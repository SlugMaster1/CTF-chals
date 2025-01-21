from secret import FLAG
from os import urandom
from Crypto.Util.number import getPrime, bytes_to_long

def genRSA():
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    return n

def rand_pad(data, bytes):
    if len(data) > bytes:
        raise OverflowError("Input data is larger than pad length")
    data += urandom(bytes-len(data))
    return data

def main():
    print("Welcome to Bring Your Own Exponent!")
    print("You may encrypt my flag three times.")
    n = genRSA()
    pad_flag = rand_pad(FLAG,127)
    print(f"Encrypting with n value: {n}")
    for i in range(3):
        print()
        while True:
            try:
                e = int(input("Enter your encryption exponent: "))
                if e.bit_length() > 16: break
                print("Enter a larger exponent")
            except ValueError:
                print("Please enter an integer")
        print("Encrypting the flag...")
        c = pow(bytes_to_long(pad_flag),e,n)
        print(f"Here is your encrypted flag: {c}")
        print(f"You have {2-i} encrypts left")
    print("Goodbye!")

if __name__ == '__main__':
    main()