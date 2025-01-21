from pwn import *

r = process('./math_playground')

r.sendline(b'711626368')
r.sendline(b'-135057195 -136584848')
#r.interactive()

# Wait for the process to crash and create a core dump
r.wait()

# Load the core file
core = r.corefile

# Print out information from the core file for debugging
print("Fault Address: 0x{:x}".format(core.fault_addr))
print("Instruction pointer: 0x{:x}".format(core.pc))
print("Stack pointer: 0x{:x}".format(core.sp))
print("Register details:")
for reg in core.arch.registers:
    print("  {} = 0x{:x}".format(reg, core.registers[reg]))

# Additional actions can be performed based on the core file content
