from math import ceil
setial = str(input())
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght * 1/8
vreme_za_otdih = break_lenght * 1/4
time_left = break_lenght - lunch_time - vreme_za_otdih

if time_left >= episode_lenght:
    time_left = abs(time_left - episode_lenght)
    print(f"You have enough time to watch {setial} and left with {ceil(time_left)} minutes free time.")
else:
    time_left = abs(time_left - episode_lenght)
    print(f"You don't have enough time to wath {setial}, you need {ceil(time_left)} more minutes ")