import math
'''
for i in range(0,5):
    for j in range(0, 2*i+1):
        print("#", end = "")
    print()
'''
# size = int(input("Enter size "))
'''
size = 10

for i in range(0, size):
    for j in range(2*size-2,-1,-1):
        if(j<i or j> int(2*size-2-i)):
            print(f" ", end="")
        else:
            print("#", end="")
    print()

size = 10
for i in range(0,size):
    for j in range(0, 2*size-1):
        if j>=(int((2*size-1)/2))-i and j<= int(((2*size-1)/2))+i:
            print ("#", end="")
        else:
            print(" ", end="")
    print()
'''

print(dir(str))