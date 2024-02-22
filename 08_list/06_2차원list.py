#2차원 리스트: [행][열]

table = [[1,2,3,4],[7,8,9,10],[10,11,12,14]]
print(table)
print(len(table)) #결과: 3
print(table[0])
#결과: [1, 2, 3, 4]

for item in table:
    print(item, type(item), len(item))
# 결과: [1, 2, 3, 4] <class 'list'> 4
# 결과: [7, 8, 9, 10] <class 'list'> 4
# 결과: [10, 11, 12, 14] <class 'list'> 4

for row in table: #[1,2,3,4]
    for col in row: #1,2,3,4
        print(col, end=' ')
    print()

# 1 2 3 4
# 7 8 9 10
# 10 11 12 14
#요소의 값을 바로 추출

row_n = len(table)
col_n = len(table[0])

for r in range(row_n):
    for c in range(col_n):
        print(table[r][c], end=' ')
        #2차원 리스트는 대괄호를 두번 씀 / 인덱스로 접근한 for문
    print()

# 1 2 3 4
# 7 8 9 10
# 10 11 12 14

#문제1: 학생별 국영수 과목별 점수와 총점, 평균 계산하고 출력
#[90,85,70] [88,79,92] [100,100,100] [90,60,70]

stud = [[90,85,70],[88,79,92],[100,100,100],[90,60,70]]
print('---성적표 (점수)---')
for row in stud:
    print(row)

print('---성적표 (점수, 총점, 평균)---')
for row in stud:
    total = sum(row)
    avg = total / len(row)
#print(f'{row}, {total}, {avg:.2f}') -> 마지막꺼만 출력됨 / 줄 간격 조심하기
    print(f'{row}, {total}, {avg:.1f}')

#code2
print('---성적표 (점수, 총점, 평균)---')
for row in stud:
    total=0
    for score in row:
        total += score
    avg = total / len(row)
    print('{0}, {1}, {2:.1f}'.format(row, total, avg))