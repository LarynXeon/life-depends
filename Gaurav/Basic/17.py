price = int(input("What's the price of the good?: "))
discount = int(input("What's the discount (num only): "))

finalPrice = price-(price*(discount/100))

print(finalPrice)