prompt = '''
 To calculate interest (Simple and Compound)
'''
import math
print(prompt)
print(math.pow(8,3))
print (8**3)
p=int(input("amount borrowed :"))
r=int(input("rate:"))
t=int(input("time (in years) :"))
simple_interest = ((p*r*t)/100)
print("simple interest is",simple_interest)

