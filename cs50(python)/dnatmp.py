    # checking number against database
    counter = 0
    iterations = len(number)
    for k in range(iterations):
        if counter == iterations:
            break
        for l in range(iterations):
                x = int(number[k])
                y = int(data[k][l])
                if x == y:
                    counter += 1
                    if counter == iterations:
                        break
                elif counter == iterations:
                    break
                else:
                    counter == 0
    print(counter)
    if counter == len(number):
        print("match")