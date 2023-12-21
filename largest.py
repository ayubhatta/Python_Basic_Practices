# program to find the largest number, middle number and shortest number among the three input numbers


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# largest = max(num1, num2, num3)
# smallest = min(num1, num2, num3)
# middle = (num1 + num2 + num3) - (largest + smallest)

# print("Largest number is", largest)
# print("Middle number is", middle)
# print("Smallest number is", smallest)



# using if - elif - else statement to find the largest number, middle number and shortest number among the three input numbers


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1>=num2 and num1>=num3:
    largest=num1
    if num2>=num3:
        middle=num2
        smallest=num3
    else:
        middle=num3
        smallest=num2
        
elif num2>=num1 and num2>=num3:
    largest=num2
    if num1>=num3:
        middle=num1
        smallest=num3
    else:
        middle=num3
        smallest=num1

else:
    largest=num3
    if num1>=num2:
        middle=num1
        smallest=num2
    else:
        middle=num2
        smallest=num1
        
print("Largest number is", largest)
print("Middle number is", middle)
print("Smallest number is", smallest)