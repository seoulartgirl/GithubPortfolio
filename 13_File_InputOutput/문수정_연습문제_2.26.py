#1.

f = open('s.txt', 'r')
data = f.readlines()

with open('s.txt', 'r') as f:
    data = f.readlines()
print(data)


#2.
# code1
with open('data/yesterday.txt', 'r') as f:
def word_count(filename):
    with open(filename, 'r') as f:
        yesterday = f.readlines()
    words = []
    for line in yesterday:
        line = line.split()
        for w in line:
            words.append(w.lower())

    #사용된 단어들만 추출하기 위해 세트로 변경
    wordList = list(set(words))
    wordList.sort()

    #단어별 빈도 계산을 위한 딕셔너리 생성 및 이용
    wordDict = dict()
    for w in wordList:
        wordDict[w] = words.count(w)

    for key, value in wordDict.items():
        print(f'{key}: {value}')

word_count('yesterday.txt')

#code 2
cnt_list=[]
val_list=[]
new_list=[]

with open('yesterday.txt','r') as f:
    val_list=f.readlines()

for i in val_list:

    temp=(i.strip('\n').split(' '))

    for j in temp:
        new_list.append(j.lower())

val_list=new_list
new_list=list(set(new_list))
new_list.sort(key=str.lower)

new_list.remove('')


print(new_list)

for i in new_list:
    print(f'"{i}":{val_list.count(i)}')

#code 3
path = 'yesterday.txt'
dict_word_count = {}
with open(path, 'r') as f:
    text = f.read()
    lower_text = text.lower().split()
    for word in lower_text:
        if word in dict_word_count:
            dict_word_count[word] += 1
        else:
            dict_word_count[word] = 1
    sorted_text = sorted(dict_word_count.keys())

with open(path, 'w', encoding='utf-8') as f:
    f.write('[출력 결과: 단어별 빈도]\n')
    for word in sorted_text:
        f.write(f'{word}: {dict_word_count[word]}\n')

#code 4
f = open("C:\Workspace\sources\yesterday.txt", mode='r')
lyrics = f.read()

lyrics = lyrics.lower()
words = lyrics.split()
words.sort()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("사용된 단어 목록(오름차순):")
for word in word_count:
    print(word)

print("\n단어별 빈도:")
for word, count in word_count.items():
    print(f"{word}: {count}개")

#code 5
with open('data/yesterday.txt', 'r') as f:
    data = f.read().lower().split()

word = {}
for voca in data:
    if voca in word:
        word[voca] += 1
    else:
        word[voca] = 1

for voca, count in sorted(word.items()):
    print(f'{voca} : {count}')

#-----------------------
# .strip('\n').split(' ') = .split()


#3.
#함수 정의 부분
#code1
def my_sum(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            numbers = sum(map(float, line.split()))
            f.write(str(numbers)+'\n')

my_sum('sum.txt')


#code2
def my_sum(input_file, name):
    with open(input_file,'r') as f:
        rst = ''
        for data in f.readlines():
            a = int(data.split(' ')[0])
            b = int(data.split(' ')[1])
            rst += f"{a}+{b}={a+b:.1f}\n"
        w = open(name, 'w', encoding='utf-8')
        w.write(rst)

input_file = 'data/number.txt'
my_sum(input_file, 'result.txt')



#4.
code1.
def input_member(file_name):
    while True:
        number = input('저장 1, 출력 2, 종료 q: ')
        if number == '1':
            save_input_file = input('멤버 명단을 저장할 파일명을 입력하세요.: ')
            with open(save_input_file, 'a', encoding='utf-8') as f:
                while True:
                    answer = input('멤버를 입력하세요.(종료는 q): ')
                    if answer == 'q':
                        print('저장이 완료되었습니다.')
                        break
                    f.write(f'{answer}\n')
        elif number == '2':
            save_output_file = input('멤버 명단이 저장된 파일명을 입력하세요.: ')
            output_member(save_output_file)
        else:
            break

def output_member(save_output_file):
    with open(save_output_file, 'r', encoding='utf-8') as f:
        members_list = [member.strip() for member in f.readlines()]
        print(members_list)

input_member('members.txt')

# code2
def input_member(path):
    with open(path,'w',encoding='utf-8') as f:

        while True:
            temp=(input('멤버를 입력하세요.(종료는 q) : '))
            if temp=='q':
                return
            else:
                f.write(temp+'\n')

def output_member(save):
    with open(save,'r',encoding='utf-8') as f:
        print(f.read(),end="")


while True:
    ch=input('저장 1, 출력 2, 종료 q : ')
    if ch == '1':
        path=input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(path)
    elif ch == '2':
        save=input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(save)
    elif ch== 'q':
        break