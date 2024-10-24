a1 = int(input("Put an angle: "))
a2 = int(input("Put an angle: "))
a3 = int(input("Put an angle: "))

ta = a1+a2+a3

if ta == 180:
    if a1 > 0 and a2 > 0 and a3 > 0:
        print("it's a triangle")
    else:
        print("Nah not jit")