# Question 1 - Days to go for a particular date in future.

import datetime

inputdate=input("Enter your date in YYYY/MO/DA")

formatdate=datetime.datetime.strptime(inputdate,'%Y/%m/%d')

output=datetime.datetime.now()-formatdate
print(output)


# Question 2 - Hours to go for a particular time.

#inputdate=input("Enter your date in YYYY/MO/DA")
import time
#formatdate=datetime.datetime.strftime(output,'%h')
convert = int(output.days*24)+int(time.strftime("%H", time.gmtime(output.seconds)))/3600

print(convert)

