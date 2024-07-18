from Crypto.Util.number import bytes_to_long

y = b'\x0c\x07\x9e\x8e/\xc2'
z1 = bytes_to_long(y)
print(f'Z1: {z1}')

v = 120
f = 5483762481 ^ v

h = 0.0028203971921452278
pi = 3.14
v2 = (int((h*4567234567342)/pi)%34)//30
print("v2: " , v2)
g=f*35

a1 = 899433952965498
a= a1//67 - (g+v2+f)

flag = z1 - a

print("flag:", flag)
print("a:", a)
print("v2:", v2)