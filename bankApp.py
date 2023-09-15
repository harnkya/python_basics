#efırerfhjerı

userA = {"name": "Harun KAYA",
         "balance": 3000,
         "extra_account": 2000
         }

userB = {"name": "Aysel KAYA",
         "balance": 5000,
         "extra_account": 4000
         }


def balance_inquiry(user):
    print(
        f"Your balance: {user['balance']} and your extra account balance: {user['extra_account']}. Have a good day!")


def deposit_money(user, number):
    user["balance"] += number


def withdraw(user, number):
    print(f"Hello,{user['name']}")

    if user["balance"] > number:
        user["balance"] -= number
        print(
            f"Withdrawing process completed!")
    else:
        if input("your balance is not enough. Do you want to use extra account? Y/N").capitalize() == "Y":
            if (user["balance"]+user["extra_account"]) >= number:
                number -= user["balance"]
                user["extra_account"] -= number
                user["balance"] = 0
                print(
                    f"Withdrawing process completed!")

            else:
                print("Sorry! Your total balance is not enough.")

        else:
            print("Have a good day!")

    balance_inquiry(user)


withdraw(userA, 4300)
