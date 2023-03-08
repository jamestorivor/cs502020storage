from cs50 import get_int

points = get_int("How many points did you get? ")

if points > 2:
    print("You got more points")
elif points < 2:
    print("You got less points")
else:
    print("We have the same points")