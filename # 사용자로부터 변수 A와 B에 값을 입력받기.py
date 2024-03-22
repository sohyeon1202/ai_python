# 사용자로부터 변수 A와 B에 값을 입력받기
A = float(input("첫 번째 숫자를 입력하세요: "))
B = float(input("두 번째 숫자를 입력하세요: "))

# 덧셈
sum_result = A + B
print("덧셈 결과:", sum_result)

# 뺄셈
subtract_result = A - B
print("뺄셈 결과:", subtract_result)

# 곱셈
multiply_result = A * B
print("곱셈 결과:", multiply_result)

# 나눗셈
if B != 0:
    divide_result = A / B
    print("나눗셈 결과:", divide_result)
else:
    print("0으로 나눌 수 없습니다.")
