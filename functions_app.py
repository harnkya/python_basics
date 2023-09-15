# 1- assign a function that returns the given string as many as wanted

# def printer():
#     is_finished=True
#     while is_finished:
#         string= input("Which message do you want to print? ")
#         number=int(input("How many times? "))

#         for x in range(number):
#             print(string)

#         finish_check= input("Do you want to continue? y/n ").capitalize()


#         if finish_check=="N":
#             print("Have a good day!")
#             is_finished=False

# printer()


# 2- define a function which adds the given unlimited parameters into a list

# def list_holder(*params):
#     my_list=[]

#     for x in params:
#         my_list.append(x)

#     print(my_list)

# list_holder("random string",5646,True)


# 3- find the prime numbers between given 2 numbers

# def prime_number_detecter():
#     prime_list = []
#     while True:
#         number1 = int(input("Please enter first number: "))
#         number2 = int(input("Please enter second number: "))


#         for x in range(number1, number2):

#             for i in range(2, x):
#                 if x % i == 0:
#                     break
#             else:
#                 prime_list.append(x)

#         print(
#             f"Prime numbers between {number1} and {number2} are: {prime_list}")

#         finish_check2 = (input("Do you want to continue? y/n")).capitalize()

#         if finish_check2 == "N":
#             print("Have a good day!")
#             break


# prime_number_detecter()

# 4-find all dividers of given number:

def divider_finder():

    while True:
        dividers = []
        number = int(input("Please enter the number: "))
        for i in range(2, number+1):
            if number % i == 0:
                dividers.append(i)

        print(f"The dividers of {number}: {dividers}")

        continue_check3 = input("Do you want to continue? y/n").upper()

        if continue_check3 == "N":
            print("Have a good day!")
            break


divider_finder()
