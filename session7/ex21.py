high_scores = [30, 40, 69, 96, 99]
high_scores.sort(reverse = True)

print("High scores:")
for i, score in enumerate(high_scores):
    print(i+1, '.', score)

loop = True
while loop:
    try:
       new_score = int(input("enter new score: "))
       high_scores.append(new_score)
       high_scores.sort(reverse = True)
       print("High scores:")
       for i in range(5):
          print(i+1, '.', high_scores[i])
    except ValueError:
        pass