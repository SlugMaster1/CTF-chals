from secret import FLAG

def bswap(num):
    return (num&0xff)<<24|(num&0xff00)<<8|(num&0xff0000)>>8|(num&0xff000000)>>24

def encrypt(plaintext):
    pt = int.from_bytes(plaintext,'big')
    ct = 0

    count = 0
    while pt:
        ct |= bswap(pt&0xffffffff)<<count*32
        pt >>= 32
        count += 1
    
    ct = int(bin(ct)[-1:1:-1],2)
    
    count = 0
    while count + count.bit_length() < ct.bit_length():
        ct ^= count<<count
        count += 1
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    while ct:
        ciphertext += alphabet[ct%26]
        ct //= 26
    
    return ciphertext

def main():
    enc = encrypt(FLAG)
    print(enc)

if __name__ == '__main__':
    main()