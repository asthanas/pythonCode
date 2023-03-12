print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price=0
if size == 'L':
    price = price + 25
elif size == 'M':
    price = price + 20
else:
    price = price + 15
    
if add_pepperoni == 'Y':
    if size == 'S':
        price = price + 2
    else:
        price = price + 3

if extra_cheese == 'Y':
    price = price + 1

print(f"Your final bill is: ${price}.")