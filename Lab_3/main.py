from vigenere_cipher import VigenereCipher
import re

def main():
    operation = input("Introduce the cipher operation (encrypt - e or decrypt - d): ")
    
    key = input("Enter a word of no less than 7 latin characters: ")
    while len(key) < 7:
        key = input("Enter a word of no less than 7 latin characters: ")
    
    message = input("Enter the message containing only romanian letters A-Z or a-z: ")
    while not re.match(r'[A-Za-zĂÎȘȚ]+', message):
        message = input("Enter the message containing only romanian letters A-Z or a-z: ")

    message_copy = re.sub(r'\s', '', message.upper())
    
    vc = VigenereCipher(key.upper()) 
        
    if operation == 'e':
        print(vc.encryptMessage(message_copy))
    else:
        print(vc.decryptMessage(message_copy))


if __name__ == "__main__":
    main()