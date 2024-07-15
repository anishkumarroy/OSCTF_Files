from z3 import *

# Define the variables
input1 = BitVec('input1', 32)
input2 = BitVec('input2', 32)
input3 = BitVec('input3', 32)

# Define the solver
s = Solver()

# Add the conditions
s.add(input1 + input2 == 0xdeadbeef)
s.add(input1 <= 0x6f56df65)
s.add(input2 == 0x6f56df8d)
s.add(input3 ^ input2 == 2103609845)

print(s.check())
# Check for a solution
if s.check() == sat:
    model = s.model()
    input1_value = model[input1].as_long()
    input2_value = model[input2].as_long()
    input3_value = model[input3].as_long()
    print(f'input1: {input1_value} (0x{input1_value:x})')
    print(f'input2: {input2_value} (0x{input2_value:x})')
    print(f'input3: {input3_value} (0x{input3_value:x})')
else:
    print("No solution found")
