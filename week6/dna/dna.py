import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            name = row
            database.append(name)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as f:
        dna = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    number = []
    for i in range(1, len(database[0])):
        number.append(longest_match(dna, database[0][i]))

    # TODO: Check database for matching profiles
    counter = 0
    name = 0
    # iterate over each number
    for k in range(1, len(database)):
        # iterate over every row
        for j in range(len(number)):
            # iterate over each number in number[]
            # compare each number with the corresponding number in database[]
            if number[j] == int(database[k][j+1]):
                # if number and database match, update counter by 1
                counter += 1
        # if counter = number of strs, all matched for that name,
        if counter == len(number):
            name = k
            break
        else:
            counter = 0
# if there is a match print out the name if not print out no match
    if name == 0:
        print("No match")
    else:
        print(f"{database[name][0]}")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
