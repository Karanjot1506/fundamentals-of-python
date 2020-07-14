prompt='''
To print the first ‘n’ multiples of given number.
'''
print(prompt)
import math
a=int(input("number:"))
b=int(input("multiples till what number:"))
for i in range (0,b+1,1):
    if (i%a==0):
        print(i)


