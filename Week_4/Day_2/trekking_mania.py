number_groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 =0
everest = 0

for _ in range(number_groups):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        musala += number_of_climbers
    elif number_of_climbers <= 12:
        monblan += number_of_climbers
    elif number_of_climbers <= 25:
        kilimanjaro += number_of_climbers
    elif number_of_climbers <= 40:
        k2 += number_of_climbers
    elif number_of_climbers >= 41:
        everest += number_of_climbers

total_climber = musala + monblan + kilimanjaro +k2 + everest

climb_musala = ((musala / total_climber) * 100)
climb_monblan =((monblan / total_climber) * 100)
climb_kilimanjaro = ((kilimanjaro / total_climber) * 100)
climb_k2 = ((k2 / total_climber) * 100)
climb_everest = ((everest / total_climber) * 100)

print(f"{climb_musala:.2f}%")
print(f"{climb_monblan:.2f}%")
print(f"{climb_kilimanjaro:.2f}%")
print(f"{climb_k2:.2f}%")
print(f"{climb_everest:.2f}%")
