from RSA_Signature import RSA_Signature
from ElGamal_Signature import ElGamal_Signature


def main():
    message = ''
    with open('message.txt', 'r') as file:
        message = file.read()

    print(f'Message: {message}\n')

    option = int(input('Choose the digital signature algorithm (1-RSA, 2-ElGamal): '))

    if option == 1:
        rsa = RSA_Signature()
        signature = rsa.compute_signature(message)
        print(f'\nSignature: {signature}\n')
        print(f'Validation result: {rsa.validate_signature(message, signature)}')
    else:
        elgamal = ElGamal_Signature()
        signature = elgamal.compute_signature(message)
        print(f'\nSignature: {signature}\n')
        print(f'Validation result: {elgamal.validate_signature(message, signature)}')


if __name__ == '__main__':
    main()