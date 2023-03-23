chicken_meal = int(input())
fish_meal = int(input())
vegeterian_meal = int(input())

chicken_menu_price = chicken_meal * 10.35
fish_menu_price = fish_meal * 12.40
vegeterian_menu_price = vegeterian_meal * 8.15
sum_meals = chicken_menu_price + fish_menu_price + vegeterian_menu_price

dessert_price = (sum_meals * 20) / 100
final_price = sum_meals + dessert_price + 2.50
print(final_price)