nylon = int(input())
paint = int(input())
thinner = int(input())
hours_of_work = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (paint * 0.1)) * 14.50
thinner_price = thinner * 5
materials_price = nylon_price + paint_price + thinner_price + 0.40
contractor_summ = (materials_price * 0.3) * hours_of_work
final_summ = materials_price + contractor_summ
print(final_summ)

