# 이 함수는 두가지값을 사칙연산을 해주는 함수
def abc(a, b, type):
    if type == 'add':
        return a+b
    elif type == 'sub':
        return a-b
    elif type == 'div':
        return a/b

result = abc(10, 5, 'div')
print(result)