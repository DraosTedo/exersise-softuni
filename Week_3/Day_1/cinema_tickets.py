day_of_the_week = input()
ticke_price = 0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Friday":
    ticke_price = 12
    print(ticke_price)
elif day_of_the_week == "Wednesday" or day_of_the_week == "Thursday":
    ticke_price = 14
    print(ticke_price)
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    ticke_price = 16
    print(ticke_price)
