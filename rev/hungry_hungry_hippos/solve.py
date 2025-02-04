from pwn import xor
from hashlib import sha256

def enc(inp):
    xorAccumulator = b''
    for i in range(len(inp)):
        xorAccumulator = xorAccumulator[:i*2] + xor(sha256(xorAccumulator+chr(inp[i]).encode()).digest(),xorAccumulator[i*2:]+b'\x00\x00')
    return xorAccumulator

ciphertext = bytes.fromhex('df7e37fae9835f8ce5a74cfca4b21f846274d39b264308ee3ec776f03acd3eb859b78e7e0286a9a9080b431acc68829532c7b0056b59ce491ed71f1edd86d4ff7b78076b88fdd662220ac6a578ce2cf627925d893d3f53b6bdb6fa297d4afa84d1a2')
choices = [b'']
while True:
    cc = []
    for flag in choices:
        mchoices = []
        for i in range(32,127):
            print(f'\r{choices[0].decode()+chr(i)}',end='')
            ct = enc(flag+chr(i).encode())
            if ct[len(flag)*2] == ciphertext[len(flag)*2] and ct[len(flag)*2+1] == ciphertext[len(flag)*2+1]:
                mchoices.append(flag+chr(i).encode())
        cc.append(mchoices)
    print()
    choices = []
    for c in cc:
        choices += c
    if choices[0][-1] == ord('}'):
        break
print(choices[0])
    
