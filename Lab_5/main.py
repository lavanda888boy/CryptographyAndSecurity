from RSA import RSA
from ElGamal import ElGamal


def main():
    el = ElGamal()
    print(el.public_b)
    print(el.private_a)
    print(el.masking_key)

if __name__ == '__main__':
    main()