#[문제1] 홀수 짝수 판별

#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.

def is_odd (a):
    if a % 2 == 0:
        return "짝수"
    else:
        return "홀수"

number = int(input())
print(is_odd(number))

# 딕셔너리에 멤버리스트가 존재함
# search_member_birth 라는 함수를 만든다
# 해당 함수가 하는기능 회원의 생일을 리턴 시켜주는 함수이다
# 매개변수값 총 2개가 넘어가야한다
# 첫번째 매개변수는 딕셔너리, 두번째 매개변수 이름