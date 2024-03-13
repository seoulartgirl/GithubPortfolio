#csv(comma separated value) 파일 읽기
#csv 모듈 임포트
# https://docs.python.org/ko/3/library/csv.html

import csv

# with open('data/05_scores2.csv', 'r') as f:
path = 'data/05_scores2.csv'
with open(path, 'r') as f:
    data = csv.reader(f)
    for x in data:
        print(x)

#결과:
# ['이름', '성별', '나이', '국어', '영어', '수학']
# ['홍길동', '남', '15', '90', '90', '80']
# ['성춘향', '여', '16', '80', '90', '100']


#obj = csv.writer(csvfile)
#obj.writerows(데이터/문자열 등 내용) 데이터 :csv 파일에 쓸 객체
data_list = [['구', '전체', '내국인', '외국인'],
             ['관악구', 519864, 502089, 17775],
             ['강남구', 547602, 542498, 5014],
             ['송파구', 686181, 679247, 6934],
             ['강동구', 428547, 424235, 4312]]
print(data_list)

with open('data/06_pop.csv', 'w', newline='') as f:
    obj = csv.writer(f, delimiter=',') #콤마로 구분
    obj.writerows(data_list) #한줄로 쭉 안나오고 나눠서 나옴

def writecsv(filename, datalist, encoding):
    with open(filename, 'w', encoding=encoding, newline='') as f:
        obj = csv.writer(f, delimiter=',')
        obj.writerows(data_list)

writecsv('data/pop1.csv', data_list, 'utf-8')