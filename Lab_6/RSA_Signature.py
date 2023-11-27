from RSA import RSA
from Crypto.Hash import MD2

class RSA_Signature(RSA):
    
    def __init__(self):
        super().__init__()


    def digest_message(self, message: str) -> int:
        h = MD2.new()
        h.update(message.encode('utf-8'))
        int_digest = int(h.hexdigest(), 16)

        return int_digest

    
    def compute_signature(self, message: str) -> int:
        return pow(self.digest_message(message), self.private_key, self.public_key[0])
    

    def validate_signature(self, message: str, signature: int) -> bool:
        int_digest = self.digest_message(message)
        print(f'Digested message: {int_digest}\n')
        decrypted_signature = pow(signature, self.public_key[1], self.public_key[0])

        if int_digest == decrypted_signature:
            return True
        else:
            return False