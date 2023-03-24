group_budget = int(input())
season = str(input())
number_of_fishermen = int(input())

rent = 0
discount = 0

if season == "Spring":
    rent = 3000

elif season == "Summer" or season == "Autumn":
    rent = 4200

elif season == "Winter":
    rent = 2600

if number_of_fishermen <= 6:
    rent *= 0.9

elif 7 < number_of_fishermen <= 11:
    rent *= 0.85

else:
    rent *= 0.75

if number_of_fishermen % 2 == 0:
    if season != "Autumn":
        rent *= 0.95

diff = abs(group_budget - rent)

if group_budget < rent:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")
