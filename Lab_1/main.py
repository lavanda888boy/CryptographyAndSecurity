from caesar_cipher import CaesarCipher
import re

def main():
    cipher_complexity = input("Introduce Caesar cipher complexity (simple - s or permutative - p): ")
    #operation = input("Introduce the cipher operation (encrypt or decrypt): ")
    
    permutation_key = ''
    if cipher_complexity == 'p':
        permutation_key = input("Enter a word of longer than 6 latin characters: ")
    
    key = int(input("Introduce a valid key from 1 to 25: "))
    message = input("Enter the message containing only letters A-Z or a-z: ")
    
    message_copy = re.sub(r'\s', '', message.upper())
    cc = CaesarCipher(key)
    n_alph = cc.transformAlphabetWithPermutations(permutation_key.upper())
    print(cc.encryptMessage(message_copy, n_alph))


if __name__ == "__main__":
    main()