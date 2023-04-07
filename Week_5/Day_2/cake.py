lenght = int(input())
height = int(input())

cake_piece = lenght * height

while cake_piece > 0:
    command = input()
    if command == "STOP":
        print(f"{cake_piece} pieces are left.")
        break
    cake_piece -= int(command)

if cake_piece < 0:
    print(f"No more cake left! You need {abs(cake_piece)} pieces more.")