#
# main.py - Main application to test functions of the FIPS.203 library
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#

from auxiliary.constants import Constants
from misc.Exceptions import InvalidParameterException

ZETA_BIT_REV7 = [
    1, 1729, 2580, 3289, 2642, 630, 1897, 848,
    1062, 1919, 193, 797, 2786, 3260, 569, 1746,
    296, 2447, 1339, 1476, 3046, 56, 2240, 1333,
    1426, 2094, 535, 2882, 2393, 2879, 1974, 821,
    289, 331, 3253, 1756, 1197, 2304, 2277, 2055,
    650, 1977, 2513, 632, 2865, 33, 1320, 1915,
    2319, 1435, 807, 452, 1438, 2868, 1534, 2402,
    2647, 2617, 1481, 648, 2474, 3110, 1227, 910,
    17, 2761, 583, 2649, 1637, 723, 2288, 1100,
    1409, 2662, 3281, 233, 756, 2156, 3015, 3050,
    1703, 1651, 2789, 1789, 1847, 952, 1461, 2687,
    939, 2308, 2437, 2388, 733, 2337, 268, 641,
    1584, 2298, 2037, 3220, 375, 2549, 2090, 1645,
    1063, 319, 2773, 757, 2099, 561, 2466, 2594,
    2804, 1092, 403, 1026, 1143, 2150, 2775, 886,
    1722, 1212, 1874, 1029, 2110, 2935, 885, 2154
]

ZETA_BIT_REV71 = [
    17, -17, 2761, -2761, 583, -583, 2649, -2649,
    1637, -1637, 723, -723, 2288, -2288, 1100, -1100,
    1409, -1409, 2662, -2662, 3281, -3281, 233, -233,
    756, -756, 2156, -2156, 3015, -3015, 3050, -3050,
    1703, -1703, 1651, -1651, 2789, -2789, 1789, -1789,
    1847, -1847, 952, -952, 1461, -1461, 2687, -2687,
    939, -939, 2308, -2308, 2437, -2437, 2388, -2388,
    733, -733, 2337, -2337, 268, -268, 641, -641,
    1584, -1584, 2298, -2298, 2037, -2037, 3220, -3220,
    375, -375, 2549, -2549, 2090, -2090, 1645, -1645,
    1063, -1063, 319, -319, 2773, -2773, 757, -757,
    2099, -2099, 561, -561, 2466, -2466, 2594, -2594,
    2804, -2804, 1092, -1092, 403, -403, 1026, -1026,
    1143, -1143, 2150, -2150, 2775, -2775, 886, -886,
    1722, -1722, 1212, -1212, 1874, -1874, 1029, -1029,
    2110, -2110, 2935, -2935, 885, -885, 2154, -2154
]

def NTT(f: [int]) -> [int]:
    """Calculates the NTT of a 256 coefficient polynomial

    FIPS.203 NTT, section 4.3 page 26

    :param f: 256 coefficient polynomial
    :return: The NTT transform
    """
    if len(f) != 256:
        raise InvalidParameterException(f"f should be of 256 entries. Received {len(f)}")

    f_hat = f.copy()
    i = 1

    length = 128
    while length >= 2:
        for start in range(0, 256, 2*length):
            zeta = ZETA_BIT_REV7[i]
            i += 1
            for j in range(start, start + length):
                t = (zeta * f_hat[j + length]) % Constants.q
                f_hat[j + length] = (f_hat[j] - t) % Constants.q
                f_hat[j] = (f_hat[j] + t) % Constants.q

        length = length // 2

    return f_hat


def INTT(f_hat: [int]) -> [int]:
    """Calculates the inverse NTT of a 256 coefficient polynomial

    FIPS.203 NTT, section 4.3 page 26

    :param f_hat: 256 coefficient polynomial
    :return: The INTT transform
    """
    if len(f_hat) != 256:
        raise InvalidParameterException(f"f_hat should be of 256 entries. Received {len(f_hat)}")

    INV_MULT_128 = 3303

    f = f_hat.copy()
    i = 127

    length = 2
    while length <= 128:
        for start in range(0, 256, 2*length):
            zeta = ZETA_BIT_REV7[i]
            i -= 1
            for j in range(start, start + length):
                t = f[j]
                f[j] = (t + f[j + length]) % Constants.q
                f[j + length] = (zeta*(f[j + length] - t)) % Constants.q

        length *= 2

    for i in range(0, len(f)):
        f[i] = (f[i] * INV_MULT_128) % Constants.q

    return f


def MultiplyNTTs(f_hat: [int], g_hat: [int]) -> [int]:
    """Evaluates the product of two polynomials in the Z_3329 domain

    :param f_hat: Polynomial
    :param g_hat: Polynomial
    :return: The product of h_hat and g_hat, mod X^256 + 1
    """
    if len(f_hat) != 256 or len(g_hat) != 256:
        raise InvalidParameterException(f"Polynomials with wrong size: f_hat={len(f_hat)}, g_hat={len((g_hat))}")

    z_hat = [0]*256
    for i in range(128):
        z_hat[2*i], z_hat[2*i+1] = BaseCaseMultiply(
            f_hat[2*1], f_hat[2*i+1],
            g_hat[2*i], g_hat[2*i+1],
            ZETA_BIT_REV71[i]
        )

    return z_hat


def BaseCaseMultiply(a0: int, a1: int, b0: int, b1: int, gamma: int) -> (int, int):
    """ Multiply two monomials in Z_3329 in the NTT domain

    FIPS.203, section 4.3.1 page 27

    :param a0: a0 + a1*X
    :param a1: a0 + a1*X
    :param b0: b0 + b1*X
    :param b1: b0 + b1*X
    :param gamma: Modulus of X^2 - gamma
    :return: The product of two monomials in Z_3329
    """
    c0 = (a0*b0 + a1*b1*gamma) % Constants.q
    c1 = (a0*b1 + a1*b0) % Constants.q

    return c0, c1


def SumNTTs(f_hat, g_hat) -> [int]:
    s = [(f+g) % Constants.q for f, g in zip(f_hat, g_hat)]

    return s