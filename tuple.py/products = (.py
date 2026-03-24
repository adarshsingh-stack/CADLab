products = (
    ("Laptop", 55000, 5),
    ("Mobile", 20000, 10),
    ("Tablet", 15000, 7),
    ("Headphones", 2000, 15),
    ("Keyboard", 1000, 20)
)

print("Product Details:")
for item in products:
    name = item[0]
    price = item[1]
    quantity = item[2]
    
    total_value = price * quantity
    
    print("Product:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Value:", total_value)
    print("----------------------")

prices = tuple(item[1] for item in products)
quantities = tuple(item[2] for item in products)

print("All Prices:", prices)
print("All Quantities:", quantities)

highest_price = max(prices)
lowest_price = min(prices)

print("Highest Price:", highest_price)
print("Lowest Price:", lowest_price)

expensive_products = tuple(item[0] for item in products if item[1] > 10000)
print("Expensive Products:", expensive_products)

new_product = ("Smartwatch", 8000, 12)
updated_products = products + (new_product,)

print("Updated Product List:")
for item in updated_products:
    print(item)