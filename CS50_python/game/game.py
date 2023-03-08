import random
while True:
    try:
        level = int(input("Level: "))
        if level >= 0:
            rand = random.randint(1,level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < rand :
                        print("Too small!")
                    elif guess > rand:
                        print("Too large!")
                    else:
                        print("Just right!")
                        break
                except (NameError,ValueError):
                    pass
        break
    except (NameError, ValueError):
        pass