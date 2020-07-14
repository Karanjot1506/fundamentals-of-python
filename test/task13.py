prompt='''
To count the number of vowels in user entered string.
'''
print(prompt)
counter = 0
c=input("enter the word").lower()
d= ["a", "e", "i", "o", "u"]

# I am entering a string of vowels.
for ch in c:
    if ch in d:
        counter += 1
print("Count : ",counter)
