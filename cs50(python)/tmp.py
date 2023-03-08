import sys
import csv

teams = []
# TODO: Read teams into memory from file
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for team in reader:
        team["rating"] = int(team["rating"])
        teams.append(team)

print(teams)