
from math import gcd
from pwn import remote
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import pad, unpad

r = remote('localhost', 1234, level='error')
r.recvuntil(b': ')
flag = int(r.recvline())
r.recvuntil(b': ')
r.sendline(b'hi')
r.recvuntil(b': ')
c1 = int(r.recvline())
r.recvuntil(b': ')
r.sendline(b'bye')
r.recvuntil(b': ')
c2 = int(r.recvline())

e = 3
m1 = bytes_to_long(pad(b'hi',100))
m2 = bytes_to_long(pad(b'bye',100))
n = gcd(c1**e-m1, c2**e-m2)
for i in range(2, 1000):
    while not n % i: 
        n //= i
dec = unpad(long_to_bytes(pow(flag, e, n)), 100)
print(dec.decode())