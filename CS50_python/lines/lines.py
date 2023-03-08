import sys

counter = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].rstrip().endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if not (line.lstrip().startswith("#") or line.isspace() or line.lstrip() == ""):
                        counter += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a python file")

print(counter)