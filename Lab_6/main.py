from RSA_Signature import RSA_Signature


def main():
    message = 'hello'
    rsa_sig = RSA_Signature()
    
    print(rsa_sig.validate_message(message, rsa_sig.create_signature(message)))


if __name__ == '__main__':
    main()