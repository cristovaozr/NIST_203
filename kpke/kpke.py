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
from misc.print_helper import print_poly_z256
from ntt.ntt import NTT, MultiplyNTTs, SumNTTs, INTT


class KPKE:
    def __init__(self, params: FIPS203Parameters):
        param_list = params.get_parameters()
        self.k = param_list["k"]
        self.eta1 = param_list["eta1"]
        self.eta2 = param_list["eta2"]
        self.du = param_list["du"]
        self.dv = param_list["dv"]

    def KPKE_KeyGen(self, d: bytes) -> (bytes, bytes,):
        g_ret = G(d + self.k.to_bytes(1))
        rho = g_ret[0:32]
        sigma = g_ret[32:64]
        N = 0

        A_hat = self.k * [[]]
        for i in range(self.k):
            A_hat[i] = self.k*[[]]
            for j in range(self.k):
                A_hat[i][j] = SampleNTT(rho + j.to_bytes(1) + i.to_bytes(1))
                # print_poly_z256(f"A_hat[{i}][{j}]", A_hat[i][j], 32) TODO: REMOVE

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
            # print_poly_z256(f"t_hat[{i}]", elem, 32)  TODO: REMOVE!

        ekpke = bytearray()
        for i in range(self.k):
            ekpke += ByteEncode(t_hat[i], 12)
        ekpke += rho

        dkpke = bytearray()
        for i in range(self.k):
            dkpke += ByteEncode(s_hat[i], 12)

        return ekpke, dkpke, A_hat

    def Encrypt(self, ekpke: bytes, m: bytes, r: bytes, A_hat = None) -> bytes:
        N = 0
        t_hat = []
        for i in range(self.k):
            t_hat.append(ByteDecode(ekpke[384*i:384*(i+1)], 12))
            # print_poly_z256(f"t_hat[{i}]", t_hat[i], 32) TODO: REMOVE

        rho = ekpke[384*self.k:]
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

        y_hat = []
        for i in range(self.k):
            y_hat.append(NTT(y[i]))

        u_hat = []
        for i in range(self.k):
            elem = [0]*256
            for j in range(self.k):
                u_temp = MultiplyNTTs(A_hat[j][i], y_hat[i])
                elem = SumNTTs(elem, u_temp)
            u_hat.append(elem)

        u_intt = []
        for i in range(self.k):
            u_intt.append(INTT(u_hat[i]))

        u = []
        for i in range(self.k):
            # u[i] = SumNTTs(u[i], e1[i])
            ut = [(u + e) % Constants.q for u, e in zip(u_intt[i], e1[i])]
            u.append(ut)
            # print_poly_z256(f"u[{i}]", u[i], 32)  # TODO: REMOVE

        mu = [Decompress(i, 1) for i in ByteDecode(m, 1)]

        v_hat = [0]*256
        for i in range(self.k):
            ty = MultiplyNTTs(t_hat[i], y_hat[i])
            v_hat = SumNTTs(v_hat, ty)

        v_hat_intt = INTT(v_hat)
        v = [(v_e + e2_e + mu_e) % Constants.q for v_e, e2_e, mu_e in zip(v_hat_intt, e2, mu)]
        # print_poly_z256("v", v, 32)  # TODO: REMOVE

        c1 = bytearray()
        for i in range(self.k):
            c1 += ByteEncode([Compress(u_e, self.du) for u_e in u[i]], self.du)

        c2 = ByteEncode([Compress(v_e, self.dv) for v_e in v], self.dv)

        c = c1 + c2
        return c

    def Decrypt(self, dkpke: bytes, c: bytes) -> bytes:
        c1 = c[0:32*self.du*self.k]
        c2 = c[32*self.du*self.k:32*(self.du*self.k + self.dv)]

        u_prime = []
        for i in range(self.k):
            uu_bd = ByteDecode(c1[i*32*self.du:(i+1)*32*self.du], self.du)
            uu = [Decompress(x, self.du) for x in uu_bd]
            u_prime.append(uu)
            # print_poly_z256(f"u_prime[{i}]", u_prime[i], 32)  # TODO: REMOVE

        v_prime_bd = ByteDecode(c2, self.dv)
        v_prime = [Decompress(x, self.dv) for x in v_prime_bd]
        # print_poly_z256("v_prime", v_prime, 32)  # TODO: REMOVE
        s_hat = []
        for i in range(self.k):
            ss = [Decompress(x, 12) for x in ByteDecode(dkpke[384*i:384*(i+1)], 12)]
            s_hat.append(ss)

        u_prime_hat = []
        for i in range(self.k):
            u_prime_hat.append(NTT(u_prime[i]))

        s_hat_u_prime_hat = [0]*256
        for i in range(self.k):
            t = MultiplyNTTs(s_hat[i], u_prime_hat[i])
            s_hat_u_prime_hat = SumNTTs(t, s_hat_u_prime_hat)

        s_hat_u_prime_hat_intt = INTT(s_hat_u_prime_hat)
        w = [(v_prime_e - shuphi) % Constants.q for v_prime_e, shuphi in zip(v_prime, s_hat_u_prime_hat_intt)]
        m = ByteEncode([Compress(x, 1) for x in w], 1)

        return m
