# this code is to check addition of two binary numbers.

# asking user to input the binary numbers
num1 = input("Enter the first binary number: ")  
num2 = input("Enter the second binary number: ")

max_len = max(len(num1), len(num2))

num1 = num1.zfill(max_len)
num2 = num2.zfill(max_len)

result = ''
carry = 0

# using for loop
for i in range(max_len - 1, -1, -1):
    r = int(num1[i]) + int(num2[i]) + carry
    result = str(r % 2) + result
    carry = r // 2
    
if carry:
    result = '1' + result
    
print(f"The sum of {num1} and {num2} is: {result}")
