import sys

numbers = [4, 5, 6, 7]

if 0 in numbers:
    print("Found")
    sys.exit(0)


print("Not Found")
sys.exit(1)