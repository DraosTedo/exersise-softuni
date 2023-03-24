flower_type = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
discount = 0

if flower_type == "Roses":
    price = 5
    if number_of_flowers > 80:
        discount += 0.1

elif flower_type == "Dahlias":
    price = 3.80
    if number_of_flowers > 90:
        discount += 0.15

elif flower_type == "Tulips":
    price = 2.80
    if number_of_flowers > 80:
        discount += 0.15

elif flower_type == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        discount -= 0.15

elif flower_type == "Gladiolus":
    price = 2.50
    if number_of_flowers < 80:
        discount -= 0.20

total_price = number_of_flowers * price * (1 - discount )

diff = abs(total_price - budget)


if total_price > budget:
    print(f"Not enough money, you need {diff:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {diff:.2f} leva left.")
