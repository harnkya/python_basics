
age = int(input("Please enter your age: "))
ageCheck = age >= 18
education = input("Please enter your education level: ")
education= education.title()
educationCheck = (education == "High School") or (education=="College")
 
 
if ageCheck:
    if educationCheck:
        print("You can get driver licence.")

    else:
        print("you must graduate from high school.")
else:
    print("You must be 18 years old at least,")
