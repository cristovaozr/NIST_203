#
# implementation.py - ML-KEM implementation -- the main algorithm of the ML-KEM
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#
from ..auxiliary.constants import FIPS203Parameters
from ..auxiliary.crypto_functions import H, G, J
from ..kpke.kpke import KPKE


class MLKEM:
    def __init__(self, params: FIPS203Parameters):
        self.kpke = KPKE(params)
        param_list = params.get_parameters()
        self.k = param_list["k"]
        self.eta1 = param_list["eta1"]
        self.eta2 = param_list["eta2"]
        self.du = param_list["du"]
        self.dv = param_list["dv"]

    def KeyGen_internal(self, d: bytes, z: bytes) -> (bytes, bytes):
        ek, dkpke, A_hat = self.kpke.KPKE_KeyGen(d)
        dk = dkpke + ek + H(ek) + z
        #
        # print("**** Debug")
        # print(A_hat)

        return ek, dk

    def Encaps_internal(self, ek: bytes, m: bytes) -> (bytes, bytes):
        g = G(m + H(ek))
        K = g[0:32]
        r = g[32:64]

        c = self.kpke.Encrypt(ek, m, r)
        return K, c

    def Decaps_internal(self, dk: bytes, c: bytes) -> bytes:
        dkpke = dk[0:384*self.k]
        ekpke = dk[384*self.k:768*self.k+32]
        h = dk[768*self.k+32:768*self.k+64]
        z = dk[768*self.k+64:768*self.k+96]
        m_prime = self.kpke.Decrypt(dkpke, c)
        g = G(m_prime + h)
        K_prime = g[0:32]
        r_prime = g[32:64]
        K_bar = J(z + c)
        c_prime = self.kpke.Encrypt(ekpke, m_prime, r_prime)
        if c != c_prime:
            K_prime = K_bar
            return K_prime

        return K_prime

    def KeyGen(self, d: bytes, z: bytes) -> (bytes, bytes):
        # TODO: Add code pertaining to the errors conditions
        return self.KeyGen_internal(d, z)


    def Encaps(self, ek: bytes, m: bytes) -> (bytes, bytes):
        # TODO: The parameter "m" should be generated in this function. Receiving it from outside for now
        # TODO: Add code pertaining to the errors conditions
        return self.Encaps_internal(ek, m)

    def Decaps(self, dk: bytes, c: bytes) -> bytes:
        # TODO: Add code pertaining to the errors conditions
        return self.Decaps_internal(dk, c)
