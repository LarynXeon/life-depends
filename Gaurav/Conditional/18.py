name = input("What's the product name?: ")
cp = int(input("What's the product cost?: "))
qty = int(input("whats the quantity?: "))

value = cp*qty

if value > 100:
    print("Value")
else:
    print("no value")