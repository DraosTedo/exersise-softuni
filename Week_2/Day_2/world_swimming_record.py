record = float(input())
distance = float(input())
time_per_meter = float(input())

water_resistance_distance = 15
water_resistance_time = 12.5

total_swiming_in_secons = distance * time_per_meter
additional_time_water_res = ((distance // water_resistance_distance) * water_resistance_time)

time_with_resistance = total_swiming_in_secons + additional_time_water_res
time_needed = time_with_resistance - record

if record > time_with_resistance:
    print(f"Yes, he succeeded! The new world record is {abs(time_with_resistance):.2f} seconds.")
else:
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")