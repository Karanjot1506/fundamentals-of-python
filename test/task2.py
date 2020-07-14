prompt = '''
cost quantity discount
'''
print(prompt)
a=int(input("price :"))
b=int(input("discount:"))
c = (a)-((b*a)/100)
print("your  discounted price is ",c)
print("you earned a discount of ",(b*a)/100)
