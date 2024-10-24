name = input("Name?: ")

s1 = int(input("1st subject mark?: "))
s2 = int(input("2nd subject mark?: "))
s3 = int(input("3rd subject mark?: "))
s4 = int(input("4th subject mark?: "))
s5 = int(input("5th subject mark?: "))

total = s1+s2+s3+s4+s5
prt = (total*100)/500

print(f"Total marks of {name} is: {total}/500")
print(f"Percentage of {name} is: {prt}%")

if prt > 33:
    print("He passed")
else:
    print("youre a failure")