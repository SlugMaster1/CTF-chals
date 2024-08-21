from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
from Crypto.Util.Padding import pad
FLAG = b'FFCTF{THIS_IS_A_TEST_FLAG}'

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
    
def main():
    e, n, d = genRSA()
    enc_flag = pow(bytes_to_long(pad(FLAG,100)), d, n)
    print("Hello and welcome to my RSA encryption service!")
    print()
    print(f"Here is your encrypted flag: {enc_flag}")
    print()
    while True: 
        print("What would you like to encrypt?")
        inp = input("Enter integer data: ")
        try: 
            data = long_to_bytes(int(inp))
        except:
            print("Please enter an integer")
            continue
        print(bytes_to_long(pad(data,100)))
        enc_data = pow(bytes_to_long(pad(data,100)),d,n)
        print(f"Encrypted data: {enc_data}")
        print()

if __name__ == '__main__': main()