#
# naive_algorithms.py - Naive implementations of some algorithms
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#

def fast_exp_mod(b: int, e: int, m: int) -> int:
    """Calculates b^e (mod m)

    :param b: Base of the exponential
    :param e: Exponent
    :param m: Modulus
    """

    r = 1
    b = b % m

    while e:
        if e % 2:
            r = (r * b) % m

        b = (b * b) % m
        e //= 2

    return r % m


def naive_ntt(f: [int]) -> [int]:
    if len(f) != 256:
        return []

    f_hat = []
    for i in range(0, 256):
        r = fast_exp_mod(17, i, 3329)
        elem = 0
        for j in range(0, 256):
            elem = (elem + f[j]*fast_exp_mod(r, j, 3329)) % 3329

        f_hat.append(elem)

    return f_hat


def naive_intt(f_hat: [int]) -> [int]:
    FACTOR_1_OVER_256 = 3316

    if len(f_hat) != 256:
        return []

    f = []
    for i in range(0, 256):
        r = fast_exp_mod(1175, i, 3329)
        elem = 0
        for j in range(0, 256):
            elem = (elem + f_hat[j]*fast_exp_mod(r, j, 3329))

        f.append((elem * FACTOR_1_OVER_256) % 3329)

    return f
