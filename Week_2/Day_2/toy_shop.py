trip_price = float(input())
num_puzzle = int(input())
num_doll = int(input())
num_bear = int(input())
num_minion = int(input())
num_truck = int(input())

order_sum = num_puzzle * 2.60 + num_doll * 3 + num_bear * 4.10 + num_minion * 8.20 + num_truck * 2

all_of_toys = num_truck + num_minion + num_bear + num_doll + num_puzzle

if all_of_toys >= 50:
    order_sum *= 0.75

rent = order_sum * 0.1
profit = order_sum - rent
diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

