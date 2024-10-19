import re
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Define the regex pattern (MM/DD/YYYY)
date_pattern = r'\s*\b(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{4})\b\s*'
while True:
    date = input('Date: ')
    if re.match(date_pattern, date):
        date = date.replace(' ','')
        month, day, year =date.split('/')
        # formateting
        if int(day)<10 and len(day)!=2:
            day = "0"+str(day)
        if int(month) <10 and len(month)!=2:
            month = "0"+str(month)
        print(f"{year}-{month}-{day}")
        break

    else:
        try:
            if ',' in date:
                month, day, year = date.split(" ")
                day = day.replace(",","")
                if month in months and int(day)<31:
                    if len(day)!=2: #formate days
                        day = "0" + str(day)
                    if months.index(month)<9:
                        month_index = '0' + str(months.index(month)+1)
                    else:
                        month_index  = months.index(month) +1
                    print(f"{year}-{month_index}-{day}")
                    break
        except:
            pass

