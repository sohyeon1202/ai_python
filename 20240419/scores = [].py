scores = []
while True:
  score=input("학생의 점수를 입력하세요")
  if score.isdigit():
    scores.append(int(score))
  else:
    break
print(scores)
print(sum(scores))
print(len(scores))
print(sum(scores)/len(scores))