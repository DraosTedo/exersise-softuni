pens = int(input())
markers = int(input())
cleaning = int(input())
discount = int(input())

price_for_pens = pens * 5.80
price_for_markers = markers * 7.20
price_for_cleaning = cleaning * 1.20
material_price = price_for_cleaning + price_for_markers + price_for_pens
price_with_discount = material_price -(material_price * 0.25)

print(price_with_discount)
