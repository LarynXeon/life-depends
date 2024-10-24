total = int(input("total: "))
disc = int(input("Discount: "))

if disc < 10:
    print(f"The price is: {total-(total*(disc/100))}")
else:
    print(total)