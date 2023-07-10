Grocery = {"Cornflakes": {"quantity": 15, "price": 100},
          "Muesli": {"quantity": 14, "price": 150},
          "Oats": {"quantity": 10, "price": 80},
          "Wheat Flakes": {"quantity": 5, "price": 75},
          "Granola": {"quantity": 8, "price": 125}}
print("Initial Stock:")
for item, details in Grocery.items():
    print(f"{item}: Quantity: {details['quantity']} kg, Price: {details['price']}")
print("\nStock Updation:")
item_name = input("Enter the item name: ")
if item_name in Grocery:
    quantity = int(input("Enter the new quantity: "))
    price = int(input("Enter the new price: "))
    Grocery[item_name]["quantity"] += quantity
    Grocery[item_name]["price"] += price
    print("Stock updated successfully!")
else:
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    Grocery[item_name] = {"quantity": quantity, "price": price}
    print("New stock added successfully!")
print("\nUpdated Stock:")
for item, details in Grocery.items():
    print(f"{item}: Quantity: {details['quantity']} kg, Price: {details['price']}")
