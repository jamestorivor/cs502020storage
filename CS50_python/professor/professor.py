import random

def main():
    level = get_level()
    counter = 0
    counting = 0
    score = 0
    while counter < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == sum:
                    counter += 1
                    counting = 0
                    score += 1
                    break
                else:
                    print(f"EEE")
                    counting += 1
            except ValueError:
                print(f"EEE")
                counting += 1
            if counting == 3:
                    print(f"Answer: {sum}")
                    counter += 1
                    counting = 0
                    break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except (ValueError,NameError):
            pass

def generate_integer(level):
    if level == 1:
        rand = random.randint(0,9)
    elif level == 2:
        rand = random.randint(10,99)
    else:
        rand = random.randint(100,999)
    return rand

if __name__ == "__main__":
    main()