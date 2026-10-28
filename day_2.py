product_name = "Coffee"
price = 4.50
quantity = 3
total = price * quantity
print(f"{quantity} x {product_name} = P{total:.2f}")
name = input("Product name: ")
price = float(input("Price: "))
quantity = float(input("Quantity: "))
total = price * quantity  
print(f"{name} = {price} x {quantity} = P {total:.2f}")