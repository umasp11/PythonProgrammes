from datetime import*
import calendar

#Calendar
yy=2021
mm=5
print(calendar.month(yy,mm))



now = datetime.now()
#today=date.today()

#current time
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#current datetime
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)