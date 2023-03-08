import csv
from tabulate import tabulate 
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        try:
            if sys.argv[1].rstrip().endswith(".csv"):
                with open(sys.argv[1]) as csvfile:
                    table = csv.reader(csvfile)
                    for row in table:
                        print(tabulate(table, headers = "firstrow",tablefmt="grid"))
            else:
                sys.exit("Not a csv file")
        except FileNotFoundError:
            sys.exit("File doesnt exist")
    
if __name__ == "__main__":
    main()