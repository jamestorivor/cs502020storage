import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            csvfile = open(sys.argv[1])
            newfile = open(sys.argv[2], "w")
            fieldnames = ['first', 'last', 'house']
            table = csv.DictReader(csvfile)
            writer = csv.DictWriter(newfile, fieldnames = fieldnames)
            writer.writeheader()
            for row in table:
                first , last = row["name"].split(",")
                writer.writerow({"first":first, "last": last, "house": row["house"]})
            csvfile.close()
            newfile.close()
                        
                        
        except FileNotFoundError:
            sys.exit("File doesnt exist")
    
if __name__ == "__main__":
    main()