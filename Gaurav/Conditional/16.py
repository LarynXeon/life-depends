mode = input("C or F?: ").upper()
if mode == "C":
    cel = float(input("What's celcius?: "))
    far = ((cel * (9/5)) + 32)
    print(far)
elif mode == "F":
    far = float(input("What's Farenheit?: "))
    cel = ((far - 32) * 5/9)
    print(cel)
else:
    print("invalid")