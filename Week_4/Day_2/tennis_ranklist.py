number_of_tournamets = int(input())
starting_points = int(input())

W = 0
F = 0
SF =0
tourney_won = 0
points = 0

for _ in range(number_of_tournamets):
    tournamet_place = input()
    if tournamet_place == "W":
        tourney_won += 1
        points += 2000
        points_after_tourney = starting_points + points
    elif tournamet_place == "F":
        points += 1200
        points_after_tourney = starting_points + points
    elif tournamet_place == "SF":
        points += 720
        points_after_tourney = starting_points + points

average_point = int(points / number_of_tournamets)
percent_won = (tourney_won / number_of_tournamets) * 100

print(f"Final points: {points_after_tourney}")
print(f"Average points: {average_point}")
print(f"{percent_won:.2f}%")