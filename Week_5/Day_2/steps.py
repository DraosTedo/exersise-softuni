goal = 10000
steps = 0

while steps < goal:
    command = input()
    if command == "Going home":
        step_to_home = int(input())
        steps += step_to_home
        break

    steps += int(command)

diff = abs(steps - goal)
if steps >= goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")