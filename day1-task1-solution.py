from datetime import date
#getting todays date and converting to respective weekday
date = date.today()
day = date.weekday()
if (day in range(0,5)):
  fare = 100
elif(day==5):
  fare = 60
else:
  fare = 80


if (day==0):
  day = "Mon"
elif (day==1):
  day = "Tue"
elif (day==2):
  day = "Wed"
elif(day==3):
  day = "Thur"
elif(day==4):
  day = "Fri"
elif(day==5):
  day = "sat"
elif(day==6):
  day = "Sun"
else:
  day = "Invalid day"


print("Date: ",date)
print("Day: ",day)
print("Fare: ",fare)