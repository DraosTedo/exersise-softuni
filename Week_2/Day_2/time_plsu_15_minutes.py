current_hour = int(input())
current_minutes = int(input())

total_time_in_minutes = current_hour * 60 + current_minutes + 15

hour = total_time_in_minutes // 60
minutes = total_time_in_minutes % 60

if hour > 23:
    hour = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
