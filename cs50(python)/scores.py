from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)
    # can also use score += [score] in place of append

average = sum(scores) / len(scores)
print(f"Average: {average}")