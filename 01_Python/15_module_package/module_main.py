# main

name = ''
def input_name():
    global name
    name = input('이름입력: ')
    print(f'__name__ : {__name__}')


def get_name():
    print(f'__name__ : {__name__}')
    if name == '':
        return 'noname'
    else:
        return name



if __name__ == '__main__':
    # print(f'__name__ : {__name__}')
    input_name()
    print(get_name())
