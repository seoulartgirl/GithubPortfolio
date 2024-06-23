import streamlit as st

st.title('Input Widgets!')
st.header('1. Button elements')
st.subheader('Button')
st.button('초기화', type='primary')
if st.button('안녕'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :raising_hand:')

st.subheader('Link Button')
st.link_button('google', 'https://www.google.com')

st.subheader('Page Link', divider=True)
st.page_link('app.py', label = 'Home', icon='🏠')
st.page_link('pages/1_Text_elements.py',
             label='Text elements')
st.page_link('pages/2_Data_elements.py',
             label='Data elements')
st.page_link('pages/문수정_연습문제.py',
             label='Excercise',
             disabled=True)

st.page_link('https://docs.streamlit.io/develop/api-reference',
             label='Streamlit Docs', icon='🌎')

st.subheader('Form submit_Button', divider=True)

with st.form(key='form1'):
    id = st.text_input('Id')
    pw = st.text_input('Password', type='password')
    submitted = st.form_submit_button() #'로그인' 넣으면 바뀜
    if submitted:
        st.write('id:', id, ',', 'password:', pw)

with st.form(key='form1-1'):
    id = st.text_input('Id')
    pw = st.text_input('Password', type='password')
    submitted = st.form_submit_button() #'로그인' 넣으면 바뀜
if submitted:
    st.write('id:', id, ',', 'password:', pw)

form = st.form(key='form2')
title = form.text_input('제목')
content = form.text_area('질문입력')
submit = form.form_submit_button('작성')
if submit:
    st.write('제목 :', title, ',', '질문 :', content)

st.divider()
st.header('2. Selection elements')
st.subheader('Checkbox')
agree = st.checkbox('찬성',
                    value=True,
                    label_visibility='collapsed') #True로 하면 check가 되어서 나타남
#label_visibility='collapsed' or 'hidden' -> 체크박스 라벨 안보임
if agree:
    st.write('Good!')

st.subheader('Toggle')
on = st.toggle('선택')
if on:
    st.write('on')

st.subheader('Radio')
fruit = st.radio(
    '좋아하는 과일은?',
    ['바나나', '딸기', '메론', '사과', '배'],
    captions=['웃어요', '달콤해요', '시원해요',
              '상큼해요', '즙이많아요'],
    horizontal=True,
    index=1)
if fruit:
    st.write(f'{fruit}를 선택했군요!')

st.subheader('Selectbox')
fruit = st.selectbox('과일을 선택하세요',
             ['바나나', '딸기', '사과', '메론'],
                     placeholder='과일을 선택하세요!',
                     label_visibility='collapsed',
                     index = None) #index=1 주면 딸기
st.write(f'당신이 선택한 과일은 {fruit}')


st.divider()
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()
st.subheader('Multiselect')
colors = st.multiselect('당신이 좋아하는 색상은?',
               options = ['red', 'green', 'blue', 'yellow', 'pink'],
               default=['green', 'blue'])
st.write('선택한 색상은', colors)

st.subheader('Selectslider')
color_st, color_end = st.select_slider('당신이 좋아하는 색상은',
                 options=['red', 'green', 'blue', 'yellow', 'pink',
                          'violet', 'indigo', 'orange'],
                         value=('blue', 'pink'))
st.write('당신이 좋아하는 색상은', color_st, ',', color_end)

st.subheader('cclor picker')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.header('3. Number Input elements')
st.subheader('Number input')
num = st.number_input('숫자입력', value=None,
                        format='%d', step=2,
                      placeholder='숫자를 입력하세요')
st.write(f'현재 숫자:{num}')

num = st.number_input('숫자입력', min_value=-10.0,
                      max_value=10.0, value=0.0, step=0.05,
                    format='%.2f', placeholder='숫자를 입력하세요')
st.write(f'현재 숫자: {num:.2f}')

st.subheader('slider')
age = st.slider('나이', min_value=0, max_value=100,
                value=20, step=2)
st.write(age)

scores = st.slider('점수대',
                min_value=0, max_value=100,
                value=(25, 50), step=2)
st.write(scores)

st.header('4.Text input elements')
st.subheader('Text input')
id = st.text_input('아이디')
pw = st.text_input('비밀번호', type='password')
st.write(f'아이디: {id}, 비밀번호: {pw}')

st.subheader('Text area')
text = st.text_area('질문을 입력하세요')
st.write(text)
st.write(f'cmd+enter를 누르면 입력된 내용이 보입니다.')
st.write(f' 총 문자 길이는 {len(text)}')

st.header('5. Date & Time input elements')
st.subheader('Date Input')

from datetime import datetime, date, time, timedelta
date = st.date_input('일자 선택', value=date(2024,3,1),
                     min_value=date(2023,1,1),
                     max_value=date(2024,12,31),
                     format='DD-MM-YYYY')
st.write(date)

st.subheader('Time Input')
time = st.time_input('시간 입력',
                     value=time(8, 00),
                     step=timedelta(minutes=30))
st.write(time)