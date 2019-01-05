# 함수의 특징
# 이름뒤에 () 괄호가 붙는다
# 함수에는 매개변수값을 넣어줘도 안넣어줘도 된다
# 함수를 만들때는 def로 만든다 다른언어같은경우에는 function으로 정의를 많이함
# 함수의 목적중 가장 큰이유는 재사용성
# return은 있을수도 없을수도 있다
# sum을 호출하면 sum은 값이 들어온걸 확인하고 로직이 다 돌고나서 최종값을 호출한애에게 돌려준다

b = sum()

def sumByMe(a, b):
    result = a+b
    return result

a = sumByMe(1, 2)

b = sumByMe(3, 4)

