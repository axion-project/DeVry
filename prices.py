# Michael Morales
# CEIS 150 - Module 1

count = 0
total_price = 0

name = input("Hello, could you please tell me your full name?: " )
min_price = float(input("What is the lowest price you wish to pay?: "))
price_list = [20.0, 100.0, 50.5, 98.0, 77.4, 85.5, 25.4, 33.8, 69.8, 101.2]

for price in price_list:
    total_price += price
    if price > min_price:
        count +=1

print(f"Hello {name}, the minimum price is, {min_price}")
print(f"There are {count} price(s) greater than the minimum price")
print(f"The total price is {total_price}")