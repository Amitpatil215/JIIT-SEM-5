from typing import Dict


lines = open("OpenSourceLab/assign-3/VendingItems.txt", "r").read().split('\n')
product = {}
for eachItem in lines:
    priceAndProduct = eachItem.split("|")
    key = priceAndProduct[0].strip()
    value = priceAndProduct[1].strip()
    product[key] = value
print(product)

print("What you want to purchase")
input = input()

if input in product.keys():
    print("Thank you for your purchase. Enjoy")
else:
    print("Available Items are")
    print(product)

"""
What you want to purchase
Popcorn
Thank you for your purchase. Enjoy


What you want to purchase
vada
Available Items are
{'Potato Chips': '20', 'Popcorn': '30', 'Chocolate': '15', 'Biscuit': '10', 'Soft Drink': '12'}
"""
