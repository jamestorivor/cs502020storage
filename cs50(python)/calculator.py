import cs50

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")

z = print(x + y)

try:
    e = int(input("e: "))
except:
    print("that is not an int!")
    exit()

try:
    f = int(input("f: "))
except:
    print("that is not an int!")
    exit()

g = print( e / f )