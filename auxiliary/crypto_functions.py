#
# main.py - Main application to test functions of the FIPS.203 library
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#

import hashlib
from misc.Exceptions import InvalidParameterException


def PRF(eta: int, byte_array: bytes, b: bytes) -> bytes:
    """ Pseudorandom function (PRF)

    Returns a (eta*64)-byte array of random data
    FIPS.203 PRF function, section 4.1, page 18.

    :param eta: Either 2 or 3
    :param byte_array: A 32-byte array
    :param b: A byte
    :return: Byte array of length (eta*64)
    """

    if eta not in [2,3]:
        raise InvalidParameterException(f"eta({eta}:  not 2 or 3")

    prf_input = bytearray(33)
    prf_input[0:32] = byte_array
    prf_input[32:33] = b

    shake256 = hashlib.shake_256()
    shake256.update(prf_input)
    return shake256.digest(eta*64)


def PRF2(byte_array: bytes, b: bytes) -> bytes:
    """Pseudorandom function (PRF) for eta == 2

    Returns a 128-byte array of random data
    FIPS.203 PRF function, section 4.1, page 18.

    :param byte_array: A 32-byte array
    :param b: A byte
    :return: Byte array of length (eta*64)
    """
    return PRF(2, byte_array, b)


def PRF3(byte_array: bytes, b: bytes) -> bytes:
    """Pseudorandom function (PRF) for eta == 3

        Returns a 192-byte array of random data
        FIPS.203 PRF function, section 4.1, page 18.

        :param byte_array: A 32-byte array
        :param b: A byte
        :return: Byte array of length (eta*64)
        """
    return PRF(3, byte_array, b)


def H(s: bytes) -> bytes:
    """Hash H function

    Returns a 32-byte hash value.
    FIPS.203 PRF function, section 4.1, page 18.

    :param s: Data
    :return: The hash
    """
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(s)
    return sha3_256.digest()


def J(s: bytes) -> bytes:
    """Hash J function

    Returns a 32-byte hash value
    FIPS.203 PRF function, section 4.1, page 18.

    :param s: Data
    :return: The hash
    """
    shake_256 = hashlib.shake_256()
    shake_256.update(s)
    return shake_256.digest(32)


def G(s: bytes) -> bytes:
    """Hash G function
    Returns two 32-byte values a, b concatenated as a||b.

    FIPS.203 PRF function, section 4.1, page 19.
    """
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(s)
    return sha3_512.digest()


class XOF:
    """eXtensible Output Function (XOF) as used by FIPS.203

    FIPS.203 PRF function, section 4.1, page 19.
    """

    def __init__(self):
        self.ctx = hashlib.shake_128()

    def Init(self) -> None:
        """Initializes the context

        The current python implementation does nothing since the initialization was done in the constructor of
        the class
        FIPS.203 XOF, section 4.1, page 20.
        """

        # Initialization done when the class was constructed
        pass

    def Absorb(self, str: bytes) -> None:
        """Updates internal XOF state with data

        FIPS.203 XOF, section 4.1, page 20.

        :param str: Data (bytes)
        """
        self.ctx.update(str)

    def Squeeze(self, size_bits: int) -> bytes:
        """Gets some bits out of the XOF

        FIPS.203 XOF, section 4.1, page 20.

        :param size_bits: Number of bits to get from the XOF
        :return: Data
        """
        b = self.ctx.digest(size_bits//8)
        return b
