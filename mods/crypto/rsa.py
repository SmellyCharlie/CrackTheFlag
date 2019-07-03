from Crypto.Util.number import inverse
import binascii

def parse_int(given):
    found = -1
    if given == '':
        return found
    try:
        found = int(given)
    except ValueError:
        found = int(given, 16)
    return found

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

        #Calcualte N if not given
        if n == -1 and p != -1 and q != -1:
            n = p * q

        #Calculate p and q if possible
        if n != -1 and p != -1 and q == -1:
            q = n/p
        elif n != -1 and q != -1 and p == -1:
            p = n/q

        ### Attempt calcualting phi ###
        if p != -1 and q != -1:
            phi = (p-1) * (q - 1)
        
        ### Attempt Classical Decryption ###
        if d == -1 and phi != -1: 
            d = inverse(e, phi)

        if n != -1 and d != -1:
            m = pow(c, d, n)
            print_message(m)
            return

def print_message(m):
    print("Plaintext: " + bytes.fromhex(str(hex(m))[2:]).decode('utf-8'))