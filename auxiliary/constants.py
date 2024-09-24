#
# main.py - Main application to test functions of the FIPS.203 library
#
# Author: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>, <cristovaozr@gmail.com>
#
# License: Please see LICENSE file for the licensing of this work
#

from abc import ABCMeta, abstractmethod


class Constants:
    """Constants class"""

    q = 3329
    """Prime for Z_q finite field"""

    zeta = 17
    """Root of unity for Z_q finite field"""

class FIPS203Parameters(metaclass=ABCMeta):
    @abstractmethod
    def get_parameters(self):
        yield None


class FIPS203MLKEM512(FIPS203Parameters):
    def get_parameters(self):
        return {
            "k": 2,
            "eta1": 3,
            "eta2": 2,
            "du": 10,
            "dv": 4
        }

class FIPS203MLKEM768(FIPS203Parameters):
    def get_parameters(self):
        return {
            "k": 3,
            "eta1": 2,
            "eta2": 2,
            "du": 10,
            "dv": 4
        }


class FIPS203MLKEM1024(FIPS203Parameters):
    def get_parameters(self):
        return {
            "k": 4,
            "eta1": 3,
            "eta2": 2,
            "du": 11,
            "dv": 5
        }


