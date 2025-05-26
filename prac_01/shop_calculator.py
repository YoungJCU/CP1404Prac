"""
CP1404 shop_calculator
"""
total_price=0
DISCOUNT=0.1
number_of_item=int(input("Number of items: "))
while number_of_item<0:
    print("Invalid number of items")
    number_of_item = int(input("Number of items: "))
    for i in range(number_of_item):
        price=float(input("Price of item: "))
        total_price=total_price+price
if total_price>100:
    total_price=total_price-total_price*DISCOUNT
print(f"Total price for {number_of_item} items is ${total_price:.2f}")