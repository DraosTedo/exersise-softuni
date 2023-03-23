lenght = int(input())
width = int(input())
height = int(input())
percent_occupied = float(input()) / 100

volume_in_cm = lenght * width * height
volume_in_liters = volume_in_cm * 0.001

water_percent = 1 - percent_occupied
water_needed = volume_in_liters * water_percent

print(water_needed)


