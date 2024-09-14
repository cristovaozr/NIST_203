#
# kpke.py - Contains function of the K-PKE component
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#

from auxiliary.constants import FIPS203Parameters, Constants
from auxiliary.crypto_functions import (G, PRF)
from auxiliary.general_algorithms import SampleNTT, SamplePolyCBD, ByteEncode, Decompress, ByteDecode, Compress
from ntt.ntt import NTT, MultiplyNTTs, SumNTTs, INTT


class KPKE:
    def __init__(self, params: FIPS203Parameters):
        param_list = params.get_parameters()
        self.k = param_list["k"]
        self.eta1 = param_list["eta1"]
        self.eta2 = param_list["eta2"]
        self.du = param_list["du"]
        self.dv = param_list["dv"]

    def KPKE_KeyGen(self, d: bytes) -> (bytes, bytes):
        g_ret = G(d + self.k.to_bytes(1))
        rho = g_ret[0:32]
        sigma = g_ret[32:64]
        N = 0

        A_hat = self.k * [[]]
        for i in range(self.k):
            A_hat[i] = self.k*[[]]
            for j in range(self.k):
                A_hat[i][j] = SampleNTT(rho + j.to_bytes(1) + i.to_bytes(1))

        s = []
        for i in range(self.k):
            s.append(SamplePolyCBD(PRF(self.eta1, sigma, N.to_bytes(1)), self.eta1))
            N += 1

        e = []
        for i in range(self.k):
            e.append(SamplePolyCBD(PRF(self.eta1, sigma, N.to_bytes(1)), self.eta1))
            N += 1

        s_hat = []
        for s_vec in s:
            s_hat.append(NTT(s_vec))

        e_hat = []
        for e_vec in e:
            e_hat.append(NTT(e_vec))

        t_hat = []
        for i in range(self.k):

            elem = [0]*256
            for j in range(self.k):
                t = MultiplyNTTs(A_hat[i][j], s_hat[j])
                elem = SumNTTs(elem, t)

            elem = SumNTTs(elem, e_hat[i])
            t_hat.append(elem)

        ekpke = bytearray()
        for i in range(self.k):
            ekpke += ByteEncode(t_hat[i], 12)
        ekpke += rho

        dkpke = bytearray()
        for i in range(self.k):
            dkpke += ByteEncode(s_hat[i], 12)

        return ekpke, dkpke

    def Encrypt(self, ekpke: bytes, m: bytes, r: bytes, A_hat = None):
        N = 0
        t_hat = []
        for i in range(self.k):
            t_hat.append(ekpke[384*i:384*(i+1)])

        rho = ekpke[:-32]
        if A_hat is None:
            A_hat = self.k * [[]]
            for i in range(self.k):
                A_hat[i] = self.k * [[]]
                for j in range(self.k):
                    A_hat[i][j] = SampleNTT(rho + j.to_bytes(1) + i.to_bytes(1))

        y = []
        for i in range(self.k):
            y.append(SamplePolyCBD(PRF(self.eta1, r, N.to_bytes(1)), self.eta1))
            N += 1

        e1 = []
        for i in range(self.k):
            e1.append(SamplePolyCBD(PRF(self.eta2, r, N.to_bytes(1)), self.eta2))
            N += 1

        e2 = SamplePolyCBD(PRF(self.eta2, r, N.to_bytes(1)), self.eta2)

        y_hat = NTT(y)
        u_hat = []
        for i in range(self.k):
            elem = [0]*256
            for j in range(self.k):
                u_temp = MultiplyNTTs(A_hat[j][i], y_hat[i])
                elem = SumNTTs(elem, u_temp)
            u_hat.append(elem)

        u = INTT(u_hat)
        u = SumNTTs(u, e1)
        mu = [Decompress(i, 1) for i in ByteDecode(m, 1)]

        v_hat = MultiplyNTTs(t_hat, y_hat)
        v_prime = INTT(v_hat)
        v = [(v_e + e2_e + mu_e) % Constants.q for v_e, e2_e, mu_e in zip(v_prime, e2, mu)]
        c1 = bytearray()
        for i in range(self.k):
            c1 += ByteEncode([Compress(u_e, self.du) for u_e in u[i]], self.du)

        c2 = ByteEncode([Compress(v_e, self.dv) for v_e in v], self.dv)

        c = c1 + c2
        return c

    def Decrypt(self, dkpke: bytes, c: bytes):
        pass
