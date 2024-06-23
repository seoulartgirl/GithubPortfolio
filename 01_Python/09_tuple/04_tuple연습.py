# 2차원 튜플 생성

#2차원 튜플의 요소를 행렬의 테이블 형식으로 출력
# 1 2 3
# 4 5 6
# 7 8 9

t = (1,2,3),(4,5,6),(7,8,9)
for t1 in t:
    for t2 in t1:
        print(t2, end=' ') # 1 2 3 4 5 6 7 8 9
    print() # 1 2 3 / 4 5 6 / 7 8 9

#결과: (1, 2, 3)
# (4, 5, 6)
# (7, 8, 9)

# print(t[0][1])

for r in range(len(t)):
    for c in range(len(t[r])):
        print(t[r][c], end=' ')
    print()

for i in range(len(t)):
    lt1,lt2,lt3=t[i]
    print(lt1,lt2,lt3)
