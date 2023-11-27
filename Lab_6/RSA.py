from sympy import randprime, mod_inverse
from math import gcd

class RSA:

    def generate_primes(self):
        p = randprime(10**461, 10**462)
        q = randprime(10**461, 10**462)
        return p, q
    
    
    def __init__(self):
        self.p, self.q = self.generate_primes()
        self.phi = (self.p - 1) * (self.q - 1)
        self.public_key = (self.p * self.q, self.generate_public_exponent())
        self.private_key = self.generate_private_key()
    

    def generate_public_exponent(self):
        e = randprime(10**4, 10**5)
        while e < self.phi:
            if gcd(e, self.phi) == 1:
                break
            else:
                e += 1
        
        return e
    

    def generate_private_key(self):
        return mod_inverse(self.public_key[1], self.phi)


    def encrypt_message(self, message: str) -> int:
        hex_message = message.encode('utf-8').hex()
        int_message = int(hex_message, 16)
        
        return pow(int_message, self.public_key[1], self.public_key[0])


    def decrypt_message(self, enc_message: int) -> str:
        dec_int_message = pow(enc_message, self.private_key, self.public_key[0])

        return bytes.fromhex(hex(dec_int_message)[2:]).decode('utf-8')

    
    def to_string(self):
        print('RSA parameters:\n')
        print(f'p = {self.p}\n')
        print(f'q = {self.q}\n')
        print(f'phi = {self.phi}\n')
        print(f'(n, e) = {self.public_key}\n')
        print(f'd = {self.private_key}\n')
