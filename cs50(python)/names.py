import sys

names = ['james', 'ron', 'kenny']

if 'ron' in names:
    print("found")
    sys.exit(0)

print("Not found")
sys.exit(1)

