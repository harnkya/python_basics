"""asking information from 3 different students without loop:"""


users = {input("Student Number: "): {
    "name": input("Name: "),
    "Surname": input("Surname: "),
    "Phone": input("Phone Number: ")
},
    input("Student Number: "): {
    "name": input("Name: "),
    "Surname": input("Surname: "),
    "Phone": input("Phone Number: ")
},
    input("Student Number: "): {
    "name": input("Name: "),
    "Surname": input("Surname: "),
    "Phone": input("Phone Number:")
}
}
print(users)

"""to show the informations of student we choose:"""

student=input("enter the number of student to be showed: ")
print(users[student])




'''                          LONG VERSION WITH .update() method:
users = {}
number = input("Please enter your student pumber: ")
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
phone = input("Please enter your phone number: ")

users.update({
    number: {
        "name": name,
        "surname": surname,
        "phone": phone
    }
})
number = input("Please enter your student pumber: ")
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
phone = input("Please enter your phone number: ")

users.update({
    number: {
        "name": name,
        "surname": surname,
        "phone": phone
    }
})

number = input("Please enter your student pumber: ")
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
phone = input("Please enter your phone number: ")

users.update({ 
    number: {
        "name": name,
        "surname": surname,
        "phone": phone
    }
})
print(users)'''
