prompt ='''
 To print number of occurrence of a given alphabet in a given string.
'''
print(prompt)
c=input("enter the word :").lower()
a=input("enter the letter to be checked :").lower()

counter =0
for ch in c:
    if ch == a:
        counter += 1
print("Count : ",counter)