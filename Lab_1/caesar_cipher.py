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


    def transformAlphabet(self):
        new_alphabet = [None] * len(self.alphabet)

        for i in range(len(self.alphabet)):
            new_alphabet[i] = self.alphabet[(i + self.key) % len(self.alphabet)]
        print(new_alphabet)

        return new_alphabet
    

    def transformAlphabetWithPermutations(self, crypto_pattern: str):
        permuted_alphabet = [None] * len(self.alphabet)

        used_letters = set()
        j = 0
        index = 0
        while j < len(crypto_pattern):
            if crypto_pattern[j] not in used_letters:
                used_letters.add(crypto_pattern[j])
                permuted_alphabet[index] = crypto_pattern[j]
                index += 1
            
            j += 1
        
        while index < len(self.alphabet):
            for k in range(len(self.alphabet)):
                if self.alphabet[k] not in used_letters:
                    permuted_alphabet[index] = self.alphabet[k]
                    index += 1

        print(permuted_alphabet)
        new_alphabet = [None] * len(self.alphabet)
        for i in range(len(self.alphabet)):
            new_alphabet[i] = permuted_alphabet[(i + self.key) % len(self.alphabet)]
        print(new_alphabet)

        return new_alphabet
