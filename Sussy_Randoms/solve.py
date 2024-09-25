import random
from pwn import remote
from sympy import isprime
from sympy.ntheory.modular import crt
from Crypto.Util.number import long_to_bytes

r = remote('localhost',12345,level='error')
p = 1
mods = []
nums = []
while p < 200:
    r.recvuntil(b"om\n")
    p += 1
    while not isprime(p): p += 1
    r.sendline(b'1')
    r.recvuntil(b': ')
    r.sendline(str(p).encode())
    r.recvuntil(b"om\n")
    r.sendline(b'2')
    res = int(r.recvline().decode())
    for i in range(200):
        random.seed(i)
        if res == random.randint(0,0xffffffff):
            break
    nums.append(i)
    mods.append(p)

print(long_to_bytes(crt(mods,nums)[0]).decode())