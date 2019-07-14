from Crypto.Util.number import inverse
import binascii
from typing import Tuple, Iterator, Iterable, Optional
import owiener
from factordb.factordb import FactorDB

def parse_int(given):
    found = -1
    if given == '':
        return found
    try:
        found = int(given)
    except ValueError:
        found = int(given, 16)
    return found

def rational_to_contfrac(e, n) -> Iterator[int]:
    while n:
        a = e // n
        yield a
        e, n = n, e - a * n

def convergents_from_contfrac(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
    n_, d_ = 1, 0
    for i, (n, d) in enumerate(contfrac_to_rational_iter(contfrac)):
        if i % 2 == 0:
            yield n + n_, d + d_
        else:
            yield n, d
        n_, d_ = n, d

def contfrac_to_rational_iter(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
    """
    ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf (6)
    """
    n0, d0 = 0, 1
    n1, d1 = 1, 0
    for q in contfrac:
        n = q * n1 + n0
        d = q * d1 + d0
        yield n, d
        n0, d0 = n1, d1
        n1, d1 = n, d

class Module():

    def __init__(self, crack):
        self.evaluate(crack)


    @classmethod
    def add_arguments(cls, crack, parser):
        parser.add_argument('--rsa-e', default="", type=str, help='exponent value for RSA cryptography')
        parser.add_argument('--rsa-n', default="", type=str, help='modulus value for RSA cryptography')
        parser.add_argument('--rsa-q', default="", type=str, help='q factor for RSA cryptography')
        parser.add_argument('--rsa-p', default="", type=str, help='p factor for RSA cryptography')
        parser.add_argument('--rsa-d', default="", type=str, help='d value for RSA cryptography')
        parser.add_argument('--rsa-c', default="", type=str, help='cipher text for RSA cryptography')
        parser.add_argument('--rsa-phi', default="", type=str, help='phi value for RSA cryptography')


    def evaluate(self, crack):
        c = parse_int(crack.config["rsa_c"])
        n = parse_int(crack.config["rsa_n"])
        p = parse_int(crack.config["rsa_p"])
        q = parse_int(crack.config["rsa_q"])
        e = parse_int(crack.config["rsa_e"])
        d = parse_int(crack.config["rsa_d"])
        phi = parse_int(crack.config["rsa_phi"])

        if c == -1:
            print("You didn't give a cipher text!")
            return

        ### Start with populating N, p and q ###

        #Try and factor N
        if n != -1:
            f = FactorDB(n)
            if not f.connect().json()['status'] == 'C':  
                primes = f.get_factor_list()
                if len(primes) == 1:
                    phi = n-1
                elif len(primes) == 2:
                    p = primes[0]
                    q = primes[1]
                else:
                    phi = 1
                    print("Multiprime, may need to check for extra factors not on FactorDB")
                    for i in primes:
                        phi = phi * (i-1)

        #Calcualte N if not given
        if n == -1 and p != -1 and q != -1:
            n = p * q

        #Calculate p and q if possible
        if n != -1 and p != -1 and q == -1:
            q = n/p
        elif n != -1 and q != -1 and p == -1:
            p = n/q

        ### Attempt calcualting phi, includes square N ###
        if p != -1 and q != -1 and phi != -1:
            if q == p:
                phi = p * (p-1)
            else:     
                phi = (p-1) * (q - 1)
        
        ### Attempt Classical Decryption ###
        if d == -1 and phi != -1: 
            d = inverse(e, phi)

        if n != -1 and d != -1:
            m = pow(c, d, n)
            print_message(m)
            return

        print("Classic RSA Failed")

        #Small E

        if n!=-1 and e !=-1 and e < 100:
            low = 0
            high = c
            while low < high:
                mid = (low+high)//2
                if mid**e < c:
                    low = mid+1
                else:
                    high = mid
            if low**e == c:
                print_message(low)
                return
            
        print("Small E attack Failed")

        #Oweiner
        if n != -1 and e != -1:
            d = owiener.attack(e,n)
            if d is None:
                d = -1
                print("Oweiner failed")
            else:
                print_message(pow(c, d, n))
                return

        #Implementation of Oweine for a few bits
        print("Attempting Wiener+ Algo")
        if n != -1 and e != -1:
            temp_m = 12345
            temp_c = pow(temp_m, e, n)
            q0 = 1
            f_ = rational_to_contfrac(e, n)
            for i in contfrac_to_rational_iter(f_):
                k = i[0]
                q1 = i[1]
                for r in range(30):
                    for s in range(30):
                        d = r*q1 + s*q0
                        m1 = pow(temp_c, d, n)
                        if m1 == temp_m:
                            print_message(pow(c, d, n))
                            return
                q0 = q1
        print("Wiener+ Failed")

        #TODO Implement: the ^0.25 version, eh it's lokey borhan but like fake, CRT
        
def print_message(m):
    print("Flag found!: " + bytes.fromhex(str(hex(m))[2:]).decode('utf-8'))