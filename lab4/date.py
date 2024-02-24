import datetime

#1
a = datetime.datetime.now()
b = a - datetime.timedelta(days=5)
print("Current Date:", a.strftime("%d-%m-%Y"))
print("Five Days Ago:", b.strftime("%d-%m-%Y"))
print()


#2
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Today:", today.strftime("%d-%m-%Y"))
print("Yesterday:", yesterday.strftime("%d-%m-%Y"))
print("Tomorrow:", tomorrow.strftime("%d-%m-%Y"))
print()


#3
date = datetime.datetime.now()
print(date.strftime("%Y-%m-%d-%H-%M-%S"))
print()


#4
date1 = datetime.datetime(*map(int, input().split()))
date2 = datetime.datetime(*map(int, input().split()))
difference = date1 - date2
print(difference.total_seconds())