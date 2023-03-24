budget = float(input())
season = input()

place = ""
discount = 0
type =  ""

if budget <= 100:
    place =  "Bulgaria"
    if season == "summer":
        type = "Camp"
        budget  *= 0.3
    if season == "winter":
        type = "Hotel"
        budget *= 0.7

elif budget <= 1000:
    place =  "Balkans"
    if season == "summer":
        type = "Camp"
        budget  *= 0.4
    if season == "winter":
        type = "Hotel"
        budget *= 0.8

elif budget > 1000:
    place =  "Europe"
    type = "Hotel"
    budget *= 0.9

print(f"Somewhere in {place}")
print(f"{type} - {budget:.2f}")
