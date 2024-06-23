# 연습문제2
# 1. iris 데이터셋을 이용
import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from konlpy.tag import Okt
import time

# 1) iris 데이터셋을 데이터프레임으로 표시
my_bar = st.progress(0, text='잠시만 기다려 주세요!')
for i in range(100):
    time.sleep(0.01)
    my_bar.progress(i+1, text='잠시만 기다려 주세요!')
time.sleep(1)
my_bar.empty()

st.divider()
st.header('1-1. iris 데이터를 dataframe으로 표시하기')
import seaborn as sns
iris = sns.load_dataset('iris')
st.dataframe(iris)

# 2) multiselect를 사용하여 품종(species)을 선택하면,
# 해당 품종의 데이터에 대한 데이터프레임으로 표시
st.divider()
st.header('1-2. multiselect를 사용하여 품종(species)을 선택하면, 해당 품종의 데이터에 대한 데이터프레임으로 표시')

species = iris.species.unique()
select = st.multiselect('데이터를 보고 싶은 품종을 선택하세요.', species)
if select:
    st.dataframe(iris[iris['species'].isin(select)])

# 3) 품종을 제외한 4가지 컬럼을 radio 요소를 사용하여 선택하면
# 선택한 컬럼에 대한 히스토그램 그리기(matplotlib)
st.divider()
st.header('1-3. 품종을 제외한 4가지 컬럼을 radio 요소를 사용하여 선택하면 선택한 컬럼에 대한 히스토그램 그리기(matplotlib)')
import matplotlib.pyplot as plt

iris1 = st.dataframe(iris[iris.columns[:-1]])
radio = st.radio('품종을 선택하세요', (iris.columns[:-1]))
if radio:
    fig, ax = plt.subplots()
    ax.hist(iris[radio])
    st.pyplot(fig)

# 2. kor_news 데이터셋을 이용
#  분류의 대분류 기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 bar chart 표시
st.divider()
st.header('2-1. 분류의 대분류 기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 bar chart 표시')
news = pd.read_excel('data/kor_news_240326.xlsx')

import re
result = []
for cat in news['분류']:
    if re.search(r'>', cat):
        result.append(cat[:re.search(r'>', cat).start()])
    else:
        result.append(cat)
news['대분류'] = result
st.dataframe(news)

select1 = st.multiselect('데이터를 보고 싶은 분야를 선택하세요.', news['대분류'].unique())
if select1:
    my_bar = st.progress(0, text='잠시만 기다려 주세요!')
    for i in range(100):
        time.sleep(0.01)
        my_bar.progress(i+1, text='잠시만 기다려 주세요!')
    time.sleep(1)
    my_bar.empty()
    df = pd.DataFrame(news[news['대분류'].isin(select1)])
    content = ' '.join(list(df['본문']))
    okt = Okt()
    token_list = [token for token, tag in okt.pos(content)
                  if (len(token) > 1) and (tag == 'Noun')]
    count = Counter(token_list)
    df1 = pd.DataFrame(pd.Series(count), columns=['Freq'])
    df1 = df1.sort_values(by='Freq', ascending=False)
    st.header(f'{str(select1)} 분야 Top 20 키워드 단어 빈도 그래프')
    st.bar_chart(data=df1.iloc[:20])


# 3. 경기도인구데이터에 대하여
# 1) 연도별 인구수에 대한 지도시각화 - 2007년, 2015년, 2019년 연도를 탭으로 제시
st.divider()
st.header('3. 연도별 인구수에 대한 지도시각화 - 2007년, 2015년, 2019년 연도를 탭으로 제시')
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import json
# from utils.map import load_data, load_geo_json, load_excel_data, draw_map (map에서 함수 가져오기)


with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
    geo_gg = json.loads(f.read())
df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')
st.dataframe(df_gg)

select2 = st.multiselect('연도를 선택하세요', (2007, 2015, 2017))
if select2:
    st.markdown(f'{select2[0]}년 경기도인구데이터')
    map = folium.Map(location=[37.5666,126.9782],
                 zoom_start=8)
    folium.GeoJson(geo_gg).add_to(map)
    folium.Choropleth(geo_data=geo_gg,
                  data=df_gg[select2[0]],
                  columns=[df_gg.index, df_gg[select2[0]]],
                  key_on='feature.properties.name').add_to(map)

    st_folium(map, width=600, height=400)