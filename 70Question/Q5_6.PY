#Question 5: A dict contains events and corresponding dates,
# given a date, find out what events have occurred and what are still pending.

import datetime

Events = {
  "2022/08/15": ["Independence Day"],
  "2022/01/26": ["Republic Day"],
  "2022/10/28": ["Lakshay's Party","NLP Quiz"]
}

Events["2022/10/14"]=["Coding club's first meet"]
print(Events)

format = '%Y/%m/%d'

events_pending=input("Enter the date in YYYY/MM/DD format.")
enterdate = datetime.datetime.strptime(events_pending, format).date()


for i in sorted(Events.keys()):
    y=datetime.datetime.strptime(i, format).date()
    if y>=enterdate:
        print(Events[i])
