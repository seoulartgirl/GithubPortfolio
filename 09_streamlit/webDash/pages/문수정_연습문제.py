# 뉴스 데이터 kor_news_240326.xlsx를 이용하여
# 스트림릿으로 구현하기
import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from konlpy.tag import Okt

# 1. 뉴스데이터를 dataframe으로 표시하기
st.header('1. 뉴스데이터를 dataframe으로 표시하기')
news = pd.read_excel('data/kor_news_240326.xlsx')
st.dataframe(news)

# def preprocess(df):
#     df['분류리스트'] = df.분류.str.split('>')
#     df['대분류'] = df['분류리스트'].str[0]
#     df['중분류'] = df['분류리스트'].str[1]
#     df['소분류'] = df['분류리스트'].str[2]
#     return df

# def load_data(file_path)
#     df = pd.read_excel(file path)
#     return preprocess(df)
# news = load_data(file_path)

# 2. 뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록
# 적절한 column configuration 사용
st.divider()
st.header('2. 뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한 column configuration 사용')

st.data_editor(news, column_config={
    'URL' : st.column_config.LinkColumn(
        help='portal site',
        max_chars=100,
        validate='^https://www\.[a-z]+\.[a-z]+',
        # display_text='Search site'
    )})

#3. 분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기
st.divider()
st.header('3.분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기')

import re

result = []
for cat in news['분류']:
    if re.search(r'>', cat):
        result.append(cat[:re.search(r'>', cat).start()])
    else:
        result.append(cat)

news['대분류'] = result
data = {cat: (len(news[(news['대분류'] == cat)])) for cat in list(news['대분류'].unique())}
df2 = pd.DataFrame(list(data.items()), columns=['category', 'value'])

st.subheader('분야별 빈도 그래프')
st.bar_chart(data=df2, x='category')

#4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로
# 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를
# bar chart로 그리기
st.divider()
st.header('4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기')

def word_count(column_name, cat_name):
    cont = list(news[news['대분류'] == cat_name][column_name])
    content = ' '.join(cont)
    okt = Okt()
    token_list = [token for token, tag in okt.pos(content)
                  if (len(token) > 1) and (tag == 'Noun')]
    count = Counter(token_list)
    df1 = pd.DataFrame(pd.Series(count), columns=['Freq'])
    df1 = df1.sort_values(by='Freq', ascending=False)
    return df1

df1 = word_count('제목', '경제')
st.header(f'Top 경제 20 단어 빈도 그래프')
st.bar_chart(data=df1.iloc[:20])

df4 = word_count('제목', '사회')
st.header(f'Top 사회 20 단어 빈도 그래프')
st.bar_chart(data=df4.iloc[:20])