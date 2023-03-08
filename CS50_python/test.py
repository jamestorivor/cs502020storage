import csv
csvfile = open("before.csv")
table = csv.DictReader(csvfile)
csvfile.close()