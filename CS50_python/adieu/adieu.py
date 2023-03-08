import inflect

p = inflect.engine()
names = []

try:
    while True:
        names.append(input("Input: "))


except EOFError:
        list = p.join(names)
        print(f"Adieu, adieu, to {list}")

