aFruitList = ["사과", "바나나"]
Fruitname = input("어떤 과일을 사고 싶으세요?")
print("{0}를 설명해드릴게요" .format(Fruitname))
if Fruitname == aFruitList[0]:
    print("사과는 3000원입니다")
elif Fruitname == aFruitList[1]:
    print("바나나는 1000원입니다")
else:
    print("그 과일은 안팝니다")

