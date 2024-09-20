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
from misc.print_helper import bytes_to_hex, print_binary, hamming, hamming2
from misc.test_vectors import PKE512_ENCRYPT_TESTS
from mlkem.mlkem import MLKEM
from ntt.ntt import (NTT, INTT, MultiplyNTTs)

from auxiliary.naive_algorithms import (naive_ntt, naive_intt)

if __name__ == "__main__":

    # mlkem = MLKEM(FIPS203MLKEM512())
    #
    # d = b'\x00'*32
    # z = b'\x00'*32
    # m = b'\x00'*32
    #
    # # Alice generates the ek and dk
    # alice_ek, alice_dk = mlkem.KeyGen(d, z)
    #
    #
    # # Alice transmits dk to Bob. Bob generates the message "m" and gets his key with the cyphered text
    # bob_K, c = mlkem.Encaps(alice_ek, m)
    # # Bob transmits c
    # # Alice generates the corresponding key from the dk and the cyphered text received from Bob
    # alice_K = mlkem.Decaps(alice_dk, c)
    # # Now Alice and Bob should have the same key: alice_K == bob_K
    #
    # print(f"Keys match: {alice_K == bob_K}")
    #
    # print_binary(alice_K)
    # print("\n\n")
    # print_binary(bob_K)
    #
    # print("\n\n")
    # xoring = bytes([a ^ b for a, b in zip(alice_K, bob_K)])
    # print_binary(xoring)
    #
    # print("\n\n")
    # print(hamming2(xoring) / 256)

    # tval = [3, 30, 300, 3000]
    # tval_comp = [Compress(t, 4) for t in tval]
    # tval2 = [Decompress(t, 4) for t in tval_comp]
    # print(tval)
    # print(tval_comp)
    # print(tval2)
    #
    # cval = [0, 1, 2, 3]
    # cval_decp = [Decompress(t, 4) for t in cval]
    # cval2 = [Compress(t, 4) for t in cval_decp]
    # print(cval)
    # print(cval_decp)
    # print(cval2)
