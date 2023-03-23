deposit_sum = float(input())
deposit_term = int(input())
year_interest_percent = float(input()) /100

nett_interes = deposit_sum * year_interest_percent
interes =nett_interes /12
total_summ = deposit_sum + deposit_term * interes
print(total_summ)