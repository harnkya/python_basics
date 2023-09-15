#                                                                 WITH DATETIME MODULE:
import datetime

date = input("When did your vehicle hit the roads? (YYYY/ MM/ DD)")
date = date.split('/')

road = datetime.datetime(int(date[0]), int(date[1]),  int(date[2]),)
difference=datetime.datetime.now() -road
days=difference.days 


if days <= 365:
    print("first maintenance term. ")
elif days < 365 and days <= 365*2:
    print("second service term.")
elif days > 365*2 and days <= 365*3:
    print("third service term")
else:
    print("please enter a vaild date")
