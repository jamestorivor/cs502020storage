while True:
    n = int(input("? x ?\n"))
    if n > 0:
        break
for i in range(n-2):
    print("#" * (n))
print("#" * n)
for i in range(n):
    print("#", end="")
print()