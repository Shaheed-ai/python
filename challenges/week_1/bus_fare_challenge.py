# WRITE YOUR CODE SOLUTION HERE
import datetime
today = datetime.date.today()
print(today)
day=(datetime.date(2021,1,29).strftime('%a'))
print(day)

import datetime

x = datetime.datetime.now().strftime("%A")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

if x in days:
    fare = 100

else:
    if x == "Saturday":
        fare = 60

    if x == "Sunday":
        fare = 80

print(fare)



