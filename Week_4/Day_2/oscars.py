actor_name = str(input())
point_from_academy = float(input())
n = int(input())

nominee_points = 1250.5

for i in range(n):
    jury_name = input()
    jury_points = float(input())
    point_from_academy += len(jury_name) * jury_points / 2

    if point_from_academy > nominee_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {point_from_academy:.1f}!")
        break

if point_from_academy <= nominee_points:
    print(f"Sorry, {actor_name} you need {nominee_points - point_from_academy:.1f} more!")
