# 시험 점수 입력 받기
score = int(input())

# 학점 계산
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score <= 89:
    grade = 'B'
elif score >= 70 and score <= 79:
    grade = 'C'
elif score >= 60 and score <= 69:
    grade = 'D'
else:
    grade = 'F'

# 학점 출력
print(grade)
