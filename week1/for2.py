result = 0
for i in range(1, 10):
    result = result + i
print(result)



marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        print("%d번 학생 축하합니다 합격입니다." % number)


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
number = 0
for i in A:
    number = number + i
average = number/len(A)
print(average)