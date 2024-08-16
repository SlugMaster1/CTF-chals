import os
os.environ['TERM'] = 'linux'

from pwn import remote
from Crypto.Util.number import long_to_bytes

def ECsubgroup(g,a,pi,p,o):
    gi = g*(o//pi)
    hi = a*(o//pi)
    c = 0
    while c < p:
        if gi*c == hi:
            return c
        c += 1
    return -1

def KDF(master_key, uid):
    user_key = master_key*uid + master_key//uid + uid
    return user_key

r = remote('localhost', 1234, level='error')
r.recvuntil(b': ')
flag_uid = Integer(r.recvline().decode())
r.recvuntil(b': ')
flag_sig = Integer(r.recvline().decode())

p = 2^255-19
E = EllipticCurve(GF(p),[0,486662,0,1,0])
o = E.order()
g, = E.gens()
b = ''
for i in range(256):
    r.recvuntil(b'signature\n')
    r.sendline(b'2')
    r.sendline(str(g.x()).encode())
    r.sendline(str(2^i).encode())
    r.recvuntil(b'is: ')
    sig = Integer(r.recvline().decode())
    sig_point = E.lift_x(sig)
    bit = ECsubgroup(g, sig_point, 2, p, o)
    b += str(bit)    
master = int(b[::-1],2)
flag_key = KDF(master, flag_uid)
inv_key = pow(flag_key, -1, o)
flag_point = E.lift_x(flag_sig)
flag = long_to_bytes(int((flag_point*inv_key).x()))
print(flag.decode())