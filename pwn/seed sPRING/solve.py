from pwn import *
from ctypes import CDLL
from math import floor
import time

libc = CDLL("libc.so.6")

# Get current time
now = floor(time.time())
libc.srand(now)

# Launch the process
#io = process('./seed_spring')
io = remote('34.125.199.248', 2534)
# Predict and send the correct values 30 times
for level_num in range(1, 31):
    io.recvuntil("Guess the height:")
    predicted_value = libc.rand() & 0xf
    print(f"Predicted value for level {level_num}: {predicted_value}")
    io.sendline(str(predicted_value))

print(io.recvline())  
print(io.recvline())
# Interact with the process to get the flag
io.interactive()
