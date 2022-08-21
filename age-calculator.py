import datetime  

def HowManyYearsDoYouLive(year,month,day):
    birthday = datetime.date(year,month,day)
    now=datetime.datetime.today()
    today=datetime.date(now.year,now.month,now.day)
    dayAlived=today-birthday
    age=int(dayAlived.days/365)
    day2=dayAlived.days-(int(dayAlived.days/365)*365)
    print("You live for ",age," years and ",day2," days")

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
HowManyYearsDoYouLive(year,month,day)
    