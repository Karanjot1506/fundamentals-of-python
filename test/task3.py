prompt = '''
To calculate cost perimeter-wise/ area-wise,
'''
print(prompt)
# considering that the figure is a square

l=int(input("size of the side of the square plot:"))

b=int(input("cost per unit length:"))
c=int(input("cost per unit area:"))

area = l*l
perimeter = 4*l

cost_perimeter_wise = perimeter*b
cost_area_wise = area*c
print("cost perimeter wise is :",cost_perimeter_wise)
print("cost area wise is :",cost_area_wise)