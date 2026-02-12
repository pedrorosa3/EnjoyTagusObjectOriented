#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


def intToTime(hour, minutes):

    """
    Convert hour and minutes to time format (HH:MM)
    
    Requires: int hour and int minutes
    Ensures: hour and minutes in time format(HH:MM)
    """

    h = int(hour)
    m = int(minutes)

    if h < 10:
        h=str(hour)
        h = "0" + h
    else:
        h=str(hour)    

    if m != 0 and m < 10:
        m=str(minutes)
        m = "0" + m
    else:
        m=str(minutes)    

    return h + ":" + m


def day_To_date(day,month):

    """
    Convert day and month to time format (DD:MM:YYYY)
    
    Requires: int day and int month
    Ensures: day and month in time format(DD:MM)
    """

    day= int(day)
    month = int(month)

    if day < 10:
        day=str(day)
        day = "0" + day
    else:
        day=str(day)
        month=str(month)    
    month=int(month)
    if month < 10:
        month=str(month)
        month = "0" + month
    else:
        day=str(day)
        month=str(month)    

    return day + ":" + month   


def Date_toInt(data_int):

    """
    Get date into a int
    """

    data_int=data_int.replace(":","")
    data_int=data_int.replace("(","")
    data_int=data_int.replace(")","")

    return int(data_int)


def Int_to_Hora(hour):

    """
    Get a int number into a hour format HH:MM
    """

    hour=str(hour)
    if len(hour)==4:
        hour_final=hour[0:2]
        minute_final=hour[2:]
    else:
        hour_final=hour[0:1]
        minute_final=hour[1:]    
    date_final=intToTime(hour_final,minute_final)

    return date_final


def DayTomoroww(date):

    """
    Next day in format DD:HH:YYYY
    """

    date=date.replace(":","")
    day=int(date[0:2])
    month=int(date[2:4])
    year=int(date[4:])

    if day ==30 and month==12:
        day="1"
        month="1"
        year=str(year+1)

        return day+":"+month+":"+year
    
    elif day==30 and month<12:
        day="1"
        month=str(month+1)
        year=str(year)

        return day+":"+month+":"+year
    
    elif day<30 :
        day=str(day+1)
        month=str(month)
        year=str(year) 

        return day_To_date(day,month)+":"+year   
    

def AfterHour(hour):

    """
    Plus 30 minutes on the previous hour in format HH:MM
    """

    hour=hour.replace(":","")
    hours=int(hour[0:2])
    minutes=int(hour[2:])
    
    if hours>=20:
        hours="08"
        minutes="00"

        return hours+":"+minutes
    
    elif hours<20 and minutes==0:
        hours=str(hours)
        minutes=str(minutes+30)

        return intToTime(hours,minutes)
    
    elif hours<20 and minutes==30:
        hours=str(hours+1)
        minutes=0

        return intToTime(hours,minutes)  


def HourToMinutes(hour):

    """
    Convert Hours in to minutes int.
    """

    hour=hour.replace(",","")
    hour=hour.replace("(","")
    hour=hour.replace(")","")
    
    if len(hour)==1:
        hour=int(hour)*100

        return  hour
    
    else:
        hours=hour[0:1]
        minutes=30
        hour=(int(hours)*100)+ minutes

        return hour


def FileNameToHour(FileName):

    """
    Convert FileName to HH:MM format
    """

    hour=FileName[-9:-4].replace("h",":")

    return hour


def FileNameToSpecification(FileName):

    """
    Convert FileName to especification of the categorie of the File and add ":" format
    EX:
    Turns "skippers10h00.txt" to Skippers:
    """
    
    categorie=(FileName[-17:-9].capitalize())+":"
    
    return categorie