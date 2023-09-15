name="Harun"
surname="Kaya"
age=20
me="I am "+ name+" "+surname+ " \nand I am "+ str(age)+" years old"
print(me)
                                               # \n =low line operator.
print(len(me))                             #len()=the length of string 
print(me[-1])            #the shortcut to get the last index of given string also if you want to go to beginning from the 
                        #end; last index starts from -1 and goes to the begin index degressively.                  

print(me[5:10])              # begin index : last index  (involves begin index but doesn't involve the last index )  

print(me[:38])               # if there is no begin index, phyton starts the first index 
print(me[0:])                 # if there is no last index, phyton types untill the last index

print(me[0:len(me)-1:3])     #types the one of every 3 characters




