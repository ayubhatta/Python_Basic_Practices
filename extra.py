# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
    
#     i += 1

# from a list of numbers, move all the zeros to the end of the list.

list = [1,0,5,0,6,7,8,9]

for i in list:
    if i==0:
        list.remove(i)
        list.append(i)
        
print(list)