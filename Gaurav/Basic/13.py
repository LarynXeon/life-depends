p = int(input("What's the base amount (principle)?: "))
r = int(input("What's the interest rate (only number)?: "))
n = int(input("What's the timeframe?: "))

I = p * (r/100) * n

print(f"Simple interest is: {I}")