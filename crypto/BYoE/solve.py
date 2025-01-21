from pwn import remote
from Crypto.Util.number import long_to_bytes

r = remote('localhost',45505,level='error')
e = 0x10001
r.recvuntil(b': ')
n = int(r.recvline().decode())
r.sendlineafter(b': ',str(e).encode())
r.recvuntil(b': ')
c1 = int(r.recvline().decode())
r.sendlineafter(b': ',str(e+1).encode())
r.recvuntil(b': ')
c2 = int(r.recvline().decode())

flag = long_to_bytes(c2*pow(c1,-1,n)%n)
print(flag)
