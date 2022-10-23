# Michael Morales
# CEIS 150 - Module 1

count =0
sum = 0
full_name = input ("What is your full name? ")
min_price = float(input("Enter the minimum price: "))
price_list = [20.0, 100.0, 50.5, 98.0, 77.4, 85.5, 25.4, 33.8, 69.8, 101.2]

for i in price_list:
    if i>min_price:
        count = count+1

for price in price_list:
    sum = sum + price
if price > min_price:
    count = count + 1
   

print ("Hello",full_name,"the minimum price is", min_price)
print ("There are",count,"prices greater than the minimum price")
print ("The total price is", sum)
