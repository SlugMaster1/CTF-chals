from Crypto.Util.number import bytes_to_long, getPrime
from Crypto.Util.Padding import pad
from secret import FLAG

def genRSA():
    e = 3
    while True:
        p = getPrime(512)
        q = getPrime(512)
        phi = (p-1)*(q-1)
        if phi % e: break
    n = p*q
    d = pow(e,-1,phi)
    return (e,n,d)
    
def encrypt(m, n, d):
    m = bytes_to_long(pad(m,100))
    c = pow(m, d, n)
    return c

def main():
    e, n, d = genRSA()
    enc_flag = encrypt(FLAG, n, d)
    print("Hello and welcome to my RSA encryption service!")
    print()
    print(f"Here is your encrypted flag: {enc_flag}")
    print()
    while True: 
        print("What would you like to encrypt?")
        inp = input("Enter some text to be encrypted: ")
        data = inp.encode()
        enc_data = encrypt(data, n, d)
        print(f"Encrypted data: {enc_data}")
        print()

if __name__ == '__main__': main()