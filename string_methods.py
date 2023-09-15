message="Hello I am Harun, I am 20 years old."

message=message.upper()    #upper() method= makes the whole string uppercase
                         #lover() method= makes the whole string 

message=message.title()   #makes uppercase the each word'S first letter               
print(message)

message=message.capitalize() # makes uppercase just the first letter of the given string, the others are lowercase
print(message)

                           #strip() = deletes the space caharacters at the beginning

message=message.split()    # splits the string from the given character and gives every splited part as a list
print(message)             # if you dont give a character to method, splits  from the space char.
message=message=' '.join(message) # reunites the string

index=message.find("years") #.find= searchs and if it finds, gives the first index of given string or character. if there is not, gives -1
print(index)

isFound=message.startswith('H')  #the usages of method startswith and endswith. give true or false values
isFound2=message.endswith('.')
print(isFound)
print(isFound2)

message=message.replace('Harun', 'harun').replace('20','21')     # usage of replace method.
print(message)

message=message.center(60,'*')    #places the string at the middle of given times '*' chararacters. Default is ' ' char.
print(message)

