time = int(input())
day_of_the_week = input()

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" or \
        day_of_the_week == "Thursday" or day_of_the_week == "Friday" or day_of_the_week == "Saturday":
    if 10 <= time <= 18:
        print("open")
    else:
        print("closed")
elif day_of_the_week == "Sunday":
    print("closed")