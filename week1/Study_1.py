aFruitList = ["사과", "바나나"]
Fruitname = input("어떤 과일을 사고 싶으세요?")
print("{0}를 설명해드릴게요" .format(Fruitname))
if Fruitname == aFruitList[0]:
    print("사과는 3000원입니다")
elif Fruitname == aFruitList[1]:
    print("바나나는 1000원입니다")
else:
    print("그 과일은 안팝니다")

친구이름 = input("친구야, 이름이 뭐니?")
나이 = input("나이는 몇살이야?")
print("안녕! {0}, 나이가 {1}이네!!" .format(친구이름,나이))


money=6000
if money < 2000:
    print("버스타라")
elif money > 5000:
    print("택시 타라")
else:
    print("걸어가라")

