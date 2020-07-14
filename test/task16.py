prompt='''
Create a dictionary of students to store names and marks obtained in 5 subjects.
'''
marks=[{"name":"karan","computers":100,"maths":100,"physics":100,"chemistry":100,"english":100}]
a = input("name")
b = int(input("marks in computers :"))
c = int(input("marks in maths :"))
d = int(input("marks in physics :"))
e = int(input("marks in chemistry :"))
f = int(input("marks in english :"))
g=[{"name":a,"computers": b,"maths":c,"physics":d,"chemistry":e,"english":f }]
marks.append(g)
print(marks)
