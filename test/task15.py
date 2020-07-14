prompt ='''
Create a dictionary to store names of states and their capitals.
'''
print(prompt)


a={"punjab":{"state":"punjab","capital":"chandigarh"}}
b=input("name of the state:")
c=input("name of the capital:")
d={b:{"state":b,"capital":c}}
a.update(d)
print(a)
