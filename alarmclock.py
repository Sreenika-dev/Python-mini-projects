import datetime    #you can additionally import playsound module

#setting alarm (please give time in the mentioned format)
alarmSet = input("Set your alarm HH:MM:SS (AM/PM): ")
setHour = alarmSet[0:2]
setMinutes = alarmSet[3:5]
setSeconds = alarmSet[6:8]
setPeriod = alarmSet[9:11].upper()   #AM and PM 
print("Alarm Set")

#comparing alarm set with our current time
while True:
    x = datetime.datetime.now()
    presentHour =  x.strftime("%I")
    presentMinute = x.strftime("%M")
    presentSecond = x.strftime("%S")
    presentPeriod = x.strftime("%p")
    if setPeriod == presentPeriod:
        if setHour == presentHour:
            if setMinutes == presentMinute:
                if setSeconds == presentSecond:
                    print("WakeUp")
                    break