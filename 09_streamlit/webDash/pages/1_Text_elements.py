import streamlit as st

st.title('Streamlit 맛보기')
st.header('1. 텍스트 요소', divider='rainbow')
st.subheader('텍스트 요소를 작성하기 위한 API', divider=True)

st.write('Hello _Streamlit_ :cool: :sunglasses:') #italic

st.write('''st.title()  
st.header()  
st.subheader()  
''') #줄바꿈하려면 두칸 띄우기

#컬러 변경 방법
st.subheader('1.2 텍스트 _본문_ 을 구성하는 :red[API]')
st.write('''
- st.write()  
- st.caption()  
- st.text()  
- st.code()  
- st.markdown()  
- st.latex()
''')

st.text('This is some text')
st.caption('This is a caption')
st.write('st.markdown()')
st.markdown('''
한줄 끝에 입력한 두 칸의 공백(space)은  
다음 줄로 사용(soft return)  

한 행에 두 개 이상의 newline은 hard return이 됨''')

sample_code = '''
def fun():
    print('Hello!!!')'''

st.write(':blue[st.code]')
st.code(sample_code, language='python')

st.write('[st.latex()]') #수식
st.latex('b \over a')
st.latex('\sqrt{x^2 + y^2}')

st.divider()
#emoji들
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.write('Emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')

st.divider()
with st.echo():
    st.write('This code will be printed')

st.divider()
with st.echo():
    def get_user_name():
        return 'john'

    def get_punctuation():
        return '!!!'

    greeting = 'Hi There!'
    user_name= get_user_name()
    punctuation = get_punctuation()
    
    st.write(greeting, user_name, punctuation)