group = int(input())
num_of_people = int(input())
n = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

mountain = ""

for i in range(n):
    current_number = int(input())
    if num_of_people <= 5:
        mountain == "Мусала"
    elif 6 <= num_of_people <= 12:
        mountain == "Монблан"
    elif 13 <= num_of_people <= 25:
        mountain == "Килиманджаро"
    elif 26 <= num_of_people <= 40:
        mountain == "К2"
    else:
        mountain == "Еверест"

