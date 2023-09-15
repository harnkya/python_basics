exam1=float(input("Enter your first exam grade: "))
exam2=float(input("Enter your second exam grade: "))
oral=float(input("Enter your second exam grade: "))

average=(exam1+exam2+oral)/3
if average>=0 and average<=100:
    print(f"your average exam grade is {average}")
    if  average>=0 and average<24:
        print("your average is: 0")
    elif average>=24 and average<44:
        print("your average is: 1") 
    elif average>=44 and average<54:
        print("your average is: 2")
    elif average>=54 and average<69:
        print("your average is: 3")
    elif average>=69 and average<84:
        print("your average is: 4")
    else:
        print("your average is: 5")    
else:
    print("Please enter valid exam grades")        