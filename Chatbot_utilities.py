##year, month, date (integer)
import re
import datetime

months = [
    r"[Jj]an(uary)?",
    r"[Ff]eb(ruary)?",
    r"[Mm]ar(ch)?",
    r"[Aa]pr(il)?",
    r"[Mm]ay",
    r"[Jj]une",
    r"[Jj]uly?",
    r"[Aa]ug(ust)?",
    r"[Ss]ept(ember)?",
    r"[Oo]ct(ober)?",
    r"[Nn]ov(ember)?",
    r"[Dd]ec(ember)?"]

weekdays = [
r"[Mm]on(day)?",
r"[Tt][Uu]es(day)?",
r"[Ww][(ED)(ed)](nesday)?",
r"[Tt][Hh]urs(day)?",
r"[Ff]ri(day)?",
r"[Ss][(AT)(at)](urday)?",
r"[Ss][(UN)(un)](day)?"]

def parseDate(arr: list) -> datetime.datetime:
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hr = now.hour
    min = now.min

    for element in arr :
        #time
        if(re.match(r"\d{1,2}:\d{2}", element)):
            idx = element.find(":")
            hr = int(element[0:idx])
            min = int(element[idx+1:])
        #year
        elif(re.match(r"\d{4}",element)):
            year = int(element)
        #day
        elif(element.isnumeric() and int(element) >= 1 and int(element) <= 31):
            day = int(element)
        else:
        #month
            for m in months :
                if(re.match(m, element)):
                    month = months.index(m) + 1

        #weekday, assuming next week (exclusive on today)
            {"""
            today is day 0, monday = 0
            set tuesday = 1
            = -1 < 0, day += 1

            today is day 0, wednesday = 2
            set tuesday = 1
            = 1 > 0, day += 7 - 1 =  6

            today is day 0, sunday = 6
            set sunday = 6
            0 = 0, day += 7 - 0 = 7 = next sunday
            """}
            for wd in weekdays :
                if(re.match(wd, element)):
                    today_date = datetime.date.today()
                    delta_day =  today_date.weekday() - weekdays.index(wd)
                    if(delta_day >= 0) :
                        day += 7 - delta_day
                    else :
                        day += delta_day

    return datetime.datetime(year, month, day, hr, min, 0, 0)

def requestDate() -> str:
    x = input("enter date time: ")
    return(parseDate(x.split()).isoformat(" "))