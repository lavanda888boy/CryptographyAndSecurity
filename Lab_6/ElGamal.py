from random import randint
from sympy import mod_inverse

class ElGamal:

    def __init__(self):
        self.p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
        self.g = 2

        self.private_b = randint(2, self.p - 2)
        self.public_b = pow(self.g, self.private_b, self.p)
        self.private_a = randint(2, self.p - 2)
        self.public_a = pow(self.g, self.private_a, self.p)


    def encrypt_message(self, message: str) -> int:
        hex_message = message.encode('utf-8').hex()
        int_message = int(hex_message, 16)
        masking_key = pow(self.public_b, self.private_a, self.p)

        return (int_message * masking_key) % self.p

    
    def decrypt_message(self, enc_message: int) -> str:
        masking_key = pow(self.public_a, self.private_b, self.p)
        masking_inverse = mod_inverse(masking_key, self.p)
        dec_int_message = (enc_message * masking_inverse) % self.p

        return bytes.fromhex(hex(dec_int_message)[2:]).decode('utf-8')

    
    def to_string(self):
        print('El Gamal parameters:\n')
        print(f'p = {self.p}\n')
        print(f'g = {self.g}\n')
        print(f'public_a = {self.public_a}\n')
        print(f'private_a = {self.private_a}\n')
        print(f'public_b = {self.public_b}\n')
        print(f'private_b = {self.private_b}\n')
