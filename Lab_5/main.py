from RSA import RSA
from ElGamal import ElGamal
from DiffieHellman import DiffieHellman

from sys import exit


def main():
    option = int(input('Choose the algorithm you would like to test (1 - RSA, 2 - El Gamal, 3 - Diffie-Hellman): '))

    algorithm = None
    if option == 1:
        algorithm = RSA()
    elif option == 2:
        algorithm = ElGamal()
    elif option == 3:
        algorithm = DiffieHellman()
    else:
        exit('Invalid option!')

    message = ''
    if option in [1, 2]:
        message = input('Enter the message you would like to encrypt/decrypt: ')

    algorithm.to_string()
    if message != '':
        encrypted_message = algorithm.encrypt_message(message)
        print(f'Encrypted message: {encrypted_message}\n')
        print(f'Decrypted message: {algorithm.decrypt_message(encrypted_message)}\n')


if __name__ == '__main__':
    main()