high_scores = [30, 40, 69, 96, 99]

print("High scores:")
for i, score in enumerate(high_scores):
    print(i+1, '.', score)

try:
    new_score = int(input("enter new score: "))
    high_scores.append(new_score)
    print("High scores:")
    for i, score in enumerate(high_scores):
        print(i+1, '.', score)
except ValueError:
    pass