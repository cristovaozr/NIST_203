#
# main.py - Main application to test functions of the FIPS.203 library
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#
from auxiliary.constants import FIPS203MLKEM512
from auxiliary.general_algorithms import *
from auxiliary.crypto_functions import *
from kpke.kpke import KPKE
from misc.print_helper import bytes_to_hex
from mlkem.mlkem import MLKEM
from ntt.ntt import (NTT, INTT, MultiplyNTTs)

from auxiliary.naive_algorithms import (naive_ntt, naive_intt)

if __name__ == "__main__":

    # my_kpke = KPKE(FIPS203MLKEM512())
    # KEYGEN_RANDOMNESS = b'\x00'*32  # 'b'0xa5'*32
    # ekpke, dkpke, A_hat = my_kpke.KPKE_KeyGen(KEYGEN_RANDOMNESS)
    #
    # print(f"{len(ekpke)=}")
    # print(f"{len(dkpke)=}")
    #
    # m = b"This is a very secret message!!!"
    # r = b'\xa5'*32
    # c = my_kpke.Encrypt(ekpke, m, r, A_hat)
    # mm = my_kpke.Decrypt(dkpke, c)
    # print(f"cyphered text={c}")
    # print(f"message={m}")
    # print(f"decoded message={mm}")

    # x = [3, 30, 300, 3000]
    # print(f"{x=}")
    # for d in range(1,12+1):
    #     x_c = [Compress(i, d) for i in x]
    #     x_c_d = [Decompress(i, d) for i in x_c]
    #     print(f"{d}: {x_c=}, {x_c_d=}")

    mlkem = MLKEM(FIPS203MLKEM512())

    d = b'\x55'*32
    z = b'\xaa'*32
    m = b'\x5a'*32

    # Alice generates the ek and dk
    alice_ek, alice_dk = mlkem.KeyGen(d, z)

    # Alice transmits dk to Bob. Bob generates the message "m" and gets his key with the cyphered text
    bob_K, c = mlkem.Encaps(alice_ek, m)
    # Bob transmits c
    # Alice generates the corresponding key from the dk and the cyphered text received from Bob
    alice_K = mlkem.Decaps(alice_dk, c)
    # Now Alice and Bob should have the same key: alice_K == bob_K

    print(alice_K == bob_K)
