import datetime
a=datetime.datetime.now().date()
print("current date is:",a)
daystoadd=int(input("enter the number of days to add"))
newdate=a+datetime.timedelta(days=daystoadd)
print("date after adding",daystoadd,"days is:",newdate)
