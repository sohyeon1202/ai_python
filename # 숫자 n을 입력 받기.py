# 숫자 n을 입력 받기
n = int(input())

# 1부터 n까지 합 구하기
total = 0
for i in range(1, n + 1):
    total += i

# 결과 출력
print(total)