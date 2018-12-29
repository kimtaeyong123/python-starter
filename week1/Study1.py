Fruitname = input("어떤 과일을 사고 싶으세요?")
print("{0}를 설명해드릴게요" .format(Fruitname))
aFruitList = ["사과", "바나나"]
for Fruitname in range(len(aFruitList)):
    if Fruitname == "사과":
        print("사과는 3000원입니다")
    elif Fruitname == "바나나":
        print("바나나는 1000원입니다")
    else:
        print("그 과일은 안팝니다")
