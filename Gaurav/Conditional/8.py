BS = int(input("What's the basic salary?: "))
DA = int(input("What's the deputation amount?: "))
HRA = int(input("What's the House rent?: "))

GS = BS + HRA + DA
print(GS)

if GS > 15000:
    print("Perma")
else:
    print("tempo")