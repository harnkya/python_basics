name="Harun"
surname="Kaya"
age=20

print("I am {} {} and I am {} years old.".format(name,surname,age))  #the usage of .format() method
print("I am {1} {2} and I am {0} years old.".format(name,surname,age)) #the other usage of .format() method
print("I am {n} {s} and I am {a} years old.".format(n=name,s=surname,a=age)) # u can use like this as well

value=300/800 #0.375
print("the value is : {v:1.2}".format(v=value)) # {v:1.2}=(one digit before the) : (the two digits before the :)
                               #python rounds up the number                    
print(f"I am {name} {surname} and I am {age} years old.")  # the usage of   f"string"




text=" random string "
print(text[::])        #prints the whole string
print(text[::-1])      #prints the string from the ending

text2="random string"*5   #you can type the string as much as you want
print(text2)
print(text.replace("r","R")) #usage of .replace method