from cs50 import get_int
# If not 1 to 8, reprompt
while True:
    height = get_int(("Height: "))
    if 0 < height < 9:
        break
# Print out staircase
i = 1
for i in range(height):
    print(" " * (height-(i+1)), end="")
    print("#" * (i+1))