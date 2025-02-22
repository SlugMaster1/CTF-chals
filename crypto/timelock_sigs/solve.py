import json
import base64
from tqdm import tqdm
from hashlib import sha256
from pwn import remote, xor

text = b'GIMME FLAG!'
r = remote('localhost', 5000)
key = b''
for i in range(len(text)):
    sig = base64.b64encode(sha256(xor(key,text[:i])+bytes([text[i]])).digest()).decode()
    for j in tqdm(range(256)):
        mes = base64.b64encode(b'\x00'*i+bytes([j])).decode()
        obj = json.dumps({'message': mes, 'signature': sig, 'time': 100})
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'> ', obj.encode())
        if b'verified' in r.recvline():
            key += bytes([j])
            break
print(len(key))
sig = base64.b64encode(sha256(key).digest()).decode()
obj = json.dumps({'message': base64.b64encode(text).decode(), 'signature': sig, 'time': 100})
r.sendlineafter(b'> ', b'2')
r.sendlineafter(b'> ', obj.encode())
r.interactive()