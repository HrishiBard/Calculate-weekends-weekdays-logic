import datetime
import calendar

mydate = input("Enter date yyyy-m-d:  ")
ymd = mydate.split('-')
mydate = datetime.date(int(ymd[0]), int(ymd[1]), int(ymd[2]))  
todayDate = datetime.date.today()
daysAbs = todayDate - mydate

weekends = []
while mydate <= todayDate:
    mydate = mydate + datetime.timedelta(1)
 
    if '5' in str(mydate.weekday()) or '6' in str(mydate.weekday()):
        print("Weekends day: ",str(mydate) + str(mydate.weekday()))
        weekends.append(str(mydate) + str(mydate.weekday()))

print("Number of weekends: ",len(weekends))
print("Working days: ",daysAbs.days - len(weekends) + 1)
