yearly_tax = int(input())
shoes = (yearly_tax * 40) / 100
equipment = (shoes * 20) / 100
ball = equipment / 4
accesories = ball / 5
final_price = yearly_tax + shoes + equipment + ball + accesories
print(final_price)
