prompt='''
To find average and grade for given marks
'''
print(prompt)
t = int(input("max marks for one subject :")) # 100
a=[] # to store marks entered by the user
num = int(input("no.of subjects :")) # 5
for x in range(0,num,1):  # x varies from 0,1,2,3,4
    marks =t+1 # 100+ 1= 101
    while marks > t: # 101 >100
        marks = int(input("enter the  marks:"))
        if marks > t:
            print("marks should be less than maximum marks")
        else:
            a.append(marks)


print("total sum is :",sum(a))
b=sum(a)
percentage = (b*100)/(num*t)
print("your percentage is ",percentage)


if (90<percentage<100):
    print("your grade is A")
elif (80<percentage<90):
    print("your grade is B")
elif (70<percentage<80):
    print("your grade is C")
elif (60<percentage<70):
    print("your grade is D")
elif (50<percentage<60):
    print("your grade is E")
else:
    print("please reappear for the exam")
