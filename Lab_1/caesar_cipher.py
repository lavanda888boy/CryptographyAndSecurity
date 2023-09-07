class CaesarCipher:

    def __init__(self, key):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.key = key


    def encryptMessage(self, message: str, new_alphabet: list):
        encrypted_message = ''

        for i in range(len(message)):
            encrypted_message += new_alphabet[self.alphabet.index(message[i])]
        
        return encrypted_message
    

    def decryptMessage(self, message: str, new_alphabet: list):
        decrypted_message = ''

        for i in range(len(message)):
            decrypted_message += self.alphabet[new_alphabet.index(message[i])]
        
        return decrypted_message


    def tranformAlphabet(self):
        new_alphabet = [None] * len(self.alphabet)

        for i in range(len(self.alphabet)):
            new_alphabet[i] = self.alphabet[(i + self.key) % len(self.alphabet)]

        return new_alphabet
