prompt = '''
To find the sum of squares of the first 100 natural numbers
'''
import  math
print(prompt)
a=[]
for i in range (0,101,1):
    x=i**2
    a.append(x)
sum(a)
print(sum(a))