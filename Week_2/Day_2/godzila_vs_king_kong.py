budget_movie = float(input())
number_statisti = int(input())
price_for_drehi_statist = float(input())

decor = budget_movie * 0.1
drehi_za_manqcite = number_statisti * price_for_drehi_statist


if number_statisti > 150:
    drehi_za_manqcite *= 0.9

total_price_za_mazniq_film = decor + drehi_za_manqcite

remaining_required = abs(budget_movie - total_price_za_mazniq_film)

if total_price_za_mazniq_film >budget_movie:
    print("Not enough money!")
    print(f"Wingard needs {remaining_required:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {remaining_required:.2f} leva left.")
