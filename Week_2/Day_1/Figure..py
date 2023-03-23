from math import pi

figure = input()

if figure == "square":
    strana = float(input())
    area = strana * strana
elif figure == "rectagle":
    strana_1 = float(input())
    strana_2 = float(input())
    area = strana_1 * strana_2
elif figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
elif figure == "triangle":
    base = float(input())
    height = float(input())
    area = 0.5 * base * height

rounded_area = round(area, 3)
print(f"{rounded_area:.3f}")


