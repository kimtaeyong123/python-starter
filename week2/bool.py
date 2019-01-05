if 1 > 5:
    print(1 > 5)

db_id = "0"

sQuery = "select * from some_table where no = 1";

result = getOne(sQuery)

# 0은 거짓 1은 참이다
# 1과 True는 0동일하게 참이다
# 0과 False는 동일하게 거짓이다

#1101 = 13