width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

while volume > 0:
    command = input()
    if command == "Done":
        print(f"{volume} Cubic meters left.")
        break

    volume -= int(command)

if volume < 0:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")