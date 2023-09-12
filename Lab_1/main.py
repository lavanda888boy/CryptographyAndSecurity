from caesar_cipher import CaesarCipher
import re

def main():
    cipher_complexity = input("Introduce Caesar cipher complexity (simple - s or permutative - p): ")
    operation = input("Introduce the cipher operation (encrypt - e or decrypt - d): ")
    
    permutation_key = ''
    if cipher_complexity == 'p':
        permutation_key = input("Enter a word of no less than 7 latin characters: ")
        while len(permutation_key) < 7:
            permutation_key = input("Enter a word of no less than 7 latin characters: ")
    
    key = int(input("Introduce a valid key from 1 to 25: "))
    while (key < 1) or (key > 25):
        key = int(input("Introduce a valid key from 1 to 25: "))

    message = input("Enter the message containing only letters A-Z or a-z: ")
    while not re.match(r'[A-Za-z]+', message):
        message = input("Enter the message containing only letters A-Z or a-z: ")

    message_copy = re.sub(r'\s', '', message.upper())
    
    cc = CaesarCipher(key)
    n_alph = []
    if cipher_complexity == 'p':
        n_alph = cc.transformAlphabetWithPermutations(permutation_key.upper())
    else:
        n_alph = cc.transformAlphabet(permutation_key.upper())    
        
    if operation == 'e':
        print(cc.encryptMessage(message_copy, n_alph))
    else:
        print(cc.decryptMessage(message_copy, n_alph))


if __name__ == "__main__":
    main()