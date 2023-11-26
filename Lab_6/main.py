from RSA_Signature import RSA_Signature
from ElGamal_Signature import ElGamal_Signature


def main():
    message = 'hello'
    elgamal = ElGamal_Signature()
    print(elgamal.compute_signature(message))


if __name__ == '__main__':
    main()