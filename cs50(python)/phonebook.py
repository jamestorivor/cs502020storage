from cs50 import get_string

people = {
    'carter': '91818777',
    'john': '91818666'
}

name = get_string("Name: ")

if name in people:
    print(f"Number: {people[name]}")