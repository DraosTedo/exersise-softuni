peters_budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

gpu_price = number_gpu *  250
gpu_to_cpu = 0.35
cpu_price = gpu_price * gpu_to_cpu
number_cpu_gpu = number_cpu * cpu_price
gpu_to_ram = 0.1

ram_price = gpu_price *gpu_to_ram
number_ram_gpu = number_ram + ram_price
final_price = gpu_price + number_cpu_gpu + number_ram_gpu

if number_gpu > number_cpu:
    final_price_discount = peters_budget -(final_price -(final_price * 0.15))
else:
    final_price_discount = peters_budget - final_price
if peters_budget >= final_price:
    print(f"You have {final_price_discount:.2f} leva left")
else:
    print(f"Not enough money! You need {abs(final_price_discount):.2f} leva more")
