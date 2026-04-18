items = ["Apple", "Banana", "Orange"]
prices = [1.50, 0.75, 2.00]
quantities = [3, 6, 2]
for quantity, item, price in zip(quantities, items, prices):
    print(f"{quantity}x {item} - ${price} each")