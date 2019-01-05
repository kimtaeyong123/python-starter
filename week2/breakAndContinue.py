# marks = [25, 90, 67, 45, 80]
#
# for mark in marks:
#     if mark > 50:
#         break
#
#     print(mark)
#
# print('aaa')

# marks = [25, 90, 67, 45, 80]
#
# for mark in marks:
#     if mark > 50:
#         break
#
#     print(mark)
#
# print('finish')

# continue의 경우 뒤에 로직을 더이상 타지 않고 다시 반복문의 첫시작으로 돌아간다
# break의 경우에는 for문을 아예 탈출 한다

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: break
    print(a)
