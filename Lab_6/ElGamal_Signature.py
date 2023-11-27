from ElGamal import ElGamal
from Crypto.Hash import MD5
from sympy import randprime, mod_inverse
from math import gcd

class ElGamal_Signature(ElGamal):

    def generate_k(self):
        k = randprime(10**4, 10**5)
        while k < self.p - 2:
            if gcd(k, self.p - 1) == 1:
                break
            else:
                k += 1
        
        return k

    
    def compute_r(self):
        return pow(self.g, self.k, self.p)

    
    def __init__(self):
        super().__init__()
        self.k = self.generate_k()
        self.r = self.compute_r()


    def digest_message(self, message: str) -> int:
        h = MD5.new()
        h.update(message.encode('utf-8'))
        int_digest = int(h.hexdigest(), 16)

        return int_digest
    

    def compute_signature(self, message: str) -> int:
        int_digest = self.digest_message(message)

        return (mod_inverse(self.k, self.p - 1) * (int_digest - self.private_a * self.r)) % (self.p - 1)
    

    def validate_signature(self, message: str, signature: int) -> bool:
        int_digest = self.digest_message(message)
        print(f'Digested message: {int_digest}\n')
        v1 = (pow(self.public_a, self.r, self.p) * pow(self.r, signature, self.p)) % self.p
        v2 = pow(self.g, int_digest, self.p)

        if v1 == v2:
            return True
        else:
            return False
