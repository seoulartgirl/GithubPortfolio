#seek(offset, whence) 함수

print('파일 내에서 검색: seek() ---')
f = open('03_seek_test_data.txt', 'r')

# f.seek(0,0) # 시작위치: 0, 0:파일의 처음
# lines = f.readlines()
# print(lines)
# f.close()

# f.seek(1,0) # 시작위치: 1, 0:파일의 처음
f.seek(3,0) # 시작위치: 4, 0:파일의 처음
lines = f.readlines()
print(lines)

f.seek(4,2) # 시작위치: 8, 0:파일의 처음
lines = f.readlines()
print(lines)

f.close()
