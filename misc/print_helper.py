#
# main.py - Main application to test functions of the FIPS.203 library
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#

def bytes_to_hex(b: bytes) -> str:
    """Converts bytes to a hex string

    :param b: Bytes array
    :return: Hexadecimal representation of the bytes array
    """

    ret = ""
    for byte in b:
        ret += f"{byte:02x}"

    return ret


def print_poly_z256(name: str = None, t: [int] = None, count_per_line: int = 16) -> None:
    if not t:
        return

    if name:
        print(f"***** {name}:")
    else:
        print("*****")

    for i in range(len(t)):
        if i and i % count_per_line == 0:
            print(f"{t[i]}")
            continue

        print(f"{t[i]}, ", end="")

    if name:
        print(f"***** {name}:")
    else:
        print("*****")


def print_binary(d: bytes) -> None:
    for i in range(len(d)*8):
        if i and i % 32 == 0:
            print("")

        if d[i//8] & 1 << (7 - (i % 8)):
            print("1", end=", ")
        else:
            print("0", end=", ")


def hamming(aa: bytes, bb: bytes) -> int:
    h = 0
    for a, b in zip(aa, bb):
        z = a ^ b
        for i in range(8):
            if z & (1 << i):
                h += 1

    return h


def hamming2(hh: bytes) -> int:
    h = 0
    for z in hh:
        for i in range(8):
            if z & (1 << i):
                h += 1

    return h