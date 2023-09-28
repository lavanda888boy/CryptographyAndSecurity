class VigenereCipher:

    def __init__(self, key):
        self.alphabet = ['A', 'Ă', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Î', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'Ș', 'T', 'Ț', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.key = key


    def encryptMessage(self, message: str):
        encrypted_message = ''

        for i in range(len(message)):
            key_index = i % len(self.key)
            encrypted_message += self.alphabet[(self.alphabet.index(message[i]) +
                                                self.alphabet.index(self.key[key_index])) %
                                                len(self.alphabet)]
        
        return encrypted_message
    

    def decryptMessage(self, message: str):
        decrypted_message = ''

        for i in range(len(message)):
            key_index = i % len(self.key)
            decrypted_message += self.alphabet[(self.alphabet.index(message[i]) -
                                                self.alphabet.index(self.key[key_index])) %
                                                len(self.alphabet)]
        
        return decrypted_message