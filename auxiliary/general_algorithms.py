#
# main.py - Main application to test functions of the FIPS.203 library
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#
from auxiliary.crypto_functions import XOF
from misc.Exceptions import InvalidParameterException
from auxiliary.constants import Constants


def BitsToBytes(b: str) -> bytes:
    """Converts a string of bits into bytes

    FIPS.203, section 4.2, page 20.

    :param b: Bits string
    :return: Array of bytes
    """
    if len(b) % 8:
        raise InvalidParameterException(f"The lenght of b({len(b)} is not a multiple of 8")

    byte_array = bytearray(len(b)//8)
    for i in range(0, len(b), 8):
        sb = b[i:i+8][::-1]
        byte_array[i // 8] = int(sb, 2)

    return byte_array


def BytesToBits(b: bytes) -> str:
    """Converts a byte array into a bit string

    FIPS.203, section 4.2, page 20.

    :param b: Byte array
    :return: Bit string
    """
    bit_str = ""
    for byte in b:
        bit_str += f"{byte:08b}"[::-1]

    return bit_str


def ByteEncode(f: [int], d: int) -> bytes:
    """Transforms a list of 256 integers into an array of bytes
    The array of bytes iS built using all 256 integers from f arranged as d-bit words

    FIPS.203, secton 4.2.1, page 22

    :param f: Polynomial coefficients
    :param d: Size in bits of the coefficient
    :return: Byte array
    """
    if d > 12 or d < 1:
        raise InvalidParameterException(f"The parameter d({d} is our of range!")

    if len(f) != 256:
        raise InvalidParameterException(f"The length of f({len(f)} is not 256!")

    enc = bytearray(32 * d)  # The size is calculated by 256 * (d/8). Since 256 // 8 is 32, then 32 * d
    enc_idx = 0
    enc_bit_idx = 0
    for c, a in enumerate(f):
        for j in range(d):
            if a % 2 == 1:
                enc[enc_idx] |= (1 << enc_bit_idx)
            a //= 2
            enc_bit_idx += 1
            if enc_bit_idx == 8:
                enc_idx += 1
                enc_bit_idx = 0

    return enc


def ByteDecode(b: bytes, d: int) -> [int]:
    """Decodes a byte array into the polynomial coefficients
    The list of coefficients are built from the d-bit words in the byte array

    FIPS.203, secton 4.2.1, page 22

    :param b:
    :param d:
    :return:
    """
    if d > 12 or d < 1:
        raise InvalidParameterException(f"The parameter d({d} is our of range!")

    if len(b) != 32*d:
        raise InvalidParameterException(f"The length of f({len(b)} is not {32*d}!")
    if d == 12:
        m = Constants.q
    else:
        m = 1 << d

    dec = [0]*256
    b_idx = 0
    b_bit_idx = 0

    for i in range(len(dec)):
        f = 0
        for j in range(d):
            if b[b_idx] & (1 << b_bit_idx):
                f += 1 << j
            b_bit_idx += 1
            if b_bit_idx == 8:
                b_idx += 1
                b_bit_idx = 0

        dec[i] = f % m

    return dec


def Compress(x: int, m: int) -> int:
    """Maps a number fom Z_3329 into Z_2^m

    FIPS.203, section 4.2, page 21

    :param x: A value from Z_3329
    :param m: A number from 1 to 12
    :return: The compressed value belonging to Z_2^m
    """
    if m > 12 or m < 1:
        raise InvalidParameterException(f"Compress m parameter invalid: ({m})")

    if m == 12:
        m = Constants.q
    else:
        m = 1 << m

    u = (m * x + 1664) // Constants.q
    return u % m


def Decompress(x: int, m: int) -> int:
    """Maps a number from Z_2^m into Z_3329

    FIPS.203, section 4.2, page 21

    :param x: A value from Z_2^m
    :param m: A number from 1 to 12
    :return: The decompressed value belonging to Z_3329
    """
    if m > 12 or m < 1:
        raise InvalidParameterException(f"Decompress m parameter invalid: ({m})")

    if m == 12:
        m = Constants.q
    else:
        m = 1 << m

    return (Constants.q * x) // m


def SampleNTT(b: bytes) -> [int]:
    """Returns an NTT sampled from T_q

    FIPS.203, section 4.2.2, page 23

    :param b: Byte array with 32 bytes and two indexes
    :return: A pseudorandom element of T_q
    """
    if len(b) != 34:
        raise InvalidParameterException(f"The size of b({len(b)}) must be 34 bytes")

    ctx = XOF()
    ctx.Init()
    ctx.Absorb(b)
    a_hat = [0]*256
    # digest = ctx.Squeeze(256*3*8)

    j = 0
    while j < 256:
        C = ctx.Squeeze(3*8)  #digest[3*j:3*(j+1)]
        c0 = C[0]
        c1 = C[1]
        c2 = C[2]
        d1 = c0 | (c1 & 0x0f) << 8
        d2 = c1 >> 4 | c2 << 4
        if d1 < Constants.q:
            a_hat[j] = d1
            j += 1
        if d2 < Constants.q and j < 256:
            a_hat[j] = d2
            j += 1

    return a_hat


def SamplePolyCBD(b: bytes, eta: int) -> [int]:
    """Samples a polynomial according to the Centered Binomial Distribution (CBD)

    FIPS.203, section 4.2.2, page 23

    :param b:
    :param eta:
    :return:
    """
    if len(b) != (64 * eta):
        raise InvalidParameterException(f"The parameter b has length {len(b)} but must be {64*eta}")

    f = [0]*256
    for i in range(256):
        x, y = 0, 0
        for j in range(eta):
            if b[(2*i*eta) // 8] & 1 << j:
                x += 1
            if b[(2*i*eta + eta) // 8] & 1 << j:
                y += 1

        f[i] = (x - y) % Constants.q

    return f
