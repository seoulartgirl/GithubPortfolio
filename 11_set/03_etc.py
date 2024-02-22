#zip() 함수
foods = ['떡볶이', '짜장면', '피자', '라면']
sides = ['김치', '단무지', '피클']

zip_list = list(zip(foods, sides))
zip_dic = dict(zip(foods,sides))
print(zip_list)
print(zip_dic)

#결과:
# [('떡볶이', '김치'), ('짜장면', '단무지'), ('피자', '피클')]
# {'떡볶이': '김치', '짜장면': '단무지', '피자': '피클'}

#리스트 컴프리헨션
xlist = [x*2 for x in range(1,11)]
print(xlist)
#결과: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

ylist = [x+y for x in range(1,11) for y in range(10,21)]
print(ylist, len(ylist))
#110개 x=10개 y= 11개

#세트 컴프리헨션
yset = {x+y for x in range(1,5) for y in range(10,15)}
print(yset, '\n' , len(yset))
#결과: {11, 12, 13, 14, 15, 16, 17, 18} / 8


foodlist = [(x,y) for x in ['밥', '국수', '짜장면']  \
            for y in ['김치', '단무지']]
print(foodlist, len(foodlist))
#결과: [('밥', '김치'), ('밥', '단무지'), ('국수', '김치'), ('국수', '단무지'), ('짜장면', '김치'), ('짜장면', '단무지')]
#총 6개 (3*2)

#딕셔너리 컴프리헨션
foods = ['떡볶이', '짜장면', '피자', '라면']
sides = ['김치', '단무지', '피클']
print({food:side for food in foods for side in sides})
#결과: {'떡볶이': '피클', '짜장면': '피클', '피자': '피클', '라면': '피클'}

stds=['철수', '영희', '길동', '순희']
std_dic ={std:0 for std in stds}
print(std_dic)
#결과: {'철수': 0, '영희': 0, '길동': 0, '순희': 0}

print(std_dic.items())
#결과: dict_items([('철수', 0), ('영희', 0), ('길동', 0), ('순희', 0)])

stds = {'철수': 90, '영희':50, '길동':60, '순희':100}
result={name:'pass' if score > 60 else 'non-pass'
        for name, score in stds.items()}
print(result)

#결과: {'철수': 'pass', '영희': 'non-pass', '길동': 'non-pass', '순희': 'pass'}

for name, score in stds.items():
    if score > 60:
        result[name]='pass'
    else:
        result[name]='non-pass'
print(result)