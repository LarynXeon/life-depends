dist = int(input("what's the distance? (km): "))
time = int(input("what's the timeframe? (hrs): "))

d = dist * 1000
t= time * 3600

vel = d/t

print(f"The velocity is: {vel} m/s")