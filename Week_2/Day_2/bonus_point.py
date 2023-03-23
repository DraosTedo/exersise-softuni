chisloto =int(input())
bonus = 0

if chisloto <= 100:
    bonus = 5
elif chisloto >= 1000:
    bonus = chisloto * 0.1
else:
    bonus = chisloto * 0.2

if chisloto % 2 == 0:
    bonus = bonus + 1
elif chisloto % 10 == 5:
    bonus = bonus + 2
print(bonus)
print(bonus + chisloto)
