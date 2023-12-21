# find and calculate square root of a number


# using exponentation operator
num1 = int(input("Enter a number:"))
sr = num1**(1/2)
print("Square root of", num1, "is", sr)

# using math module

import math
num2 = int(input("Enter a number:"))
sr2 = math.sqrt(num2)
print("Square root of", num2, "is", sr2)
