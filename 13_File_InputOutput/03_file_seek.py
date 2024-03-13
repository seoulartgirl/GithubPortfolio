#seek(offset, whence) 함수

print('파일 내에서 검색: seek() ---')
f = open('data/03_seek_test_data.txt', 'r', encoding='utf-8')

f.seek(0,0) # 시작위치: 0, 0:파일의 처음
lines = f.readlines()
print(lines)

f.seek(1,0) # 시작위치: 1, 0:파일의 처음
lines = f.readlines()
print(lines)


f.seek(3,0) # 시작위치: 3, 0:파일의 처음
lines = f.readlines()
print(lines)

f.seek(8,0) # 시작위치: 8, 0:파일의 처음
lines = f.readlines()
print(lines)

# f.seek(16,0) # 시작위치: 16, 0:파일의 처음 / utf-8은 3바이트
# lines = f.readlines()
# print(lines)

f.close()
