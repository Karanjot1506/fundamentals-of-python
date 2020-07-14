a=[]
b = int(input("no of elements in list :"))
for i in range (0,b,1):
    c=int(input("enter the number"))
    a.append(c)
a.sort()
d= b-1
print("largest no. is :",a[d])
print("smallest no. is :",a[0])