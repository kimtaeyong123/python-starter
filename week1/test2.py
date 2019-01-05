FruitList = ["apple", "banana"]
for Fruitname in FruitList:
    if Fruitname == "apple":
        print(3000)
    elif Fruitname == "banana":
        print(1000)


result = 0
for i in range(1, 10):
    result = result + i
    if result % 2 == 0:
        print(result)



a = range(11)
print(a)

pocket = ['money', 'card']
name = input()
if name in pocket:
    print("Taxi")
else:
    print("walk")