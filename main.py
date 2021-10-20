import datetime

#now = datetime.datetime.now()
#print(now)

#time = now.time()
#print(time)

#dd_mm_yyyy = now.strftime("%d-%B-%Y")
#print(dd_mm_yyyy)
#hh_mm = now.strftime("%H:%M")
#print(hh_mm)

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
MONTHS = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
while True:
    print("Enter the year for the calender:")
    year = input("> ")

    if year.isdecimal():
        if int(year) > 0:
            year = int(year)
        break

while True:
    print("Enter the month for the calendar")
    month = input("> ")

    if not month.isdecimal():
        print("Enter a number")
        continue

    month = int(month)
    if 1 <= month <= 12:
        break

    print("type 1 - 12")

calendar_text = f"{MONTHS[month]} {year}".center(80)
calendar_text += "\n...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"
week_sep = "+----------"*7
blank_row = "|          "*7
#calendar_text += blank_row + "|"


current_date = datetime.date(year, month, 1)


while current_date.weekday() != 6:
    current_date -= datetime.timedelta(days=1)

while True:
    calendar_text += week_sep + '+'
    day_number_row = ''
    for i in range(7):
        if len(str(current_date.day)) < 2:
            day_number_label = f"0{str(current_date.day)}"
        else :
            day_number_label = str(current_date.day)

        day_number_row += "|" + day_number_label + " "*8
        current_date += datetime.timedelta(days=1)

    day_number_row += '|\n'
    calendar_text += f"\n{day_number_row}"


    for i in range (3):
        calendar_text += blank_row + "|\n"

    if current_date.month != month:
        calendar_text += week_sep + "+"
        break

print(calendar_text)
calendar_text += week_sep + "+"