import streamlit as st
import pandas as pd
import numpy as np

st.title('Metric')

st.metric(label='온도', value='22°C', delta='1.2°C')
st.metric(label='체감온도', value='23°C', delta='1.1°C')
st.metric(label='풍속', value='9mph', delta='-8%')

st.divider()
col1, col2, col3 = st.columns(3)
col1.metric(label='온도', value='22°C', delta='1.2°C')
col2.metric(label='체감온도', value='23°C', delta='1.1°C')
col3.metric(label='풍속', value='9mph', delta='-8%')

st.divider()
col1, col2= st.columns(2)
col1.metric(label='온도', value='22°C', delta='1.2°C',
            delta_color='inverse')
col2.metric(label='풍속', value='9mph', delta='-8%',
            delta_color='inverse')

st.divider()
col1, col2= st.columns(2)
col1.metric(label='온도', value='22°C', delta='1.2°C',
            delta_color='normal')
col2.metric(label='풍속', value='9mph', delta='-8%',
            delta_color='normal')

st.divider()
col1, col2= st.columns(2)
col1.metric(label='온도', value='22°C', delta='1.2°C',
            delta_color='off')
col2.metric(label='풍속', value='9mph', delta='-8%',
            delta_color='off')

st.divider()
st.title('Chart')
st.header('1. Bar Chart')

df = pd.DataFrame(np.random.rand(20,3),
                  columns=['A','B','C'])
st.dataframe(df)


st.bar_chart(df)
st.bar_chart(df['A'])
st.bar_chart(df, y='A')

df2 = pd.DataFrame({'A': list(range(20)),
                    'B': np.random.rand(20),
                    'C': ['x']*5 +['y']*5 + ['z']*5 +['s']*5})

st.dataframe(df2)
st.bar_chart(df2, x='A', y='B')
st.bar_chart(df2, x='A', y='B', color='C')
st.bar_chart(df2, x='A', y='B', color='#ff0000')
st.bar_chart(df, x='A', y=['B','C'], color=['#ff0000','#0000ff'])

st.header('2. Line Chart')
st.line_chart(df)
st.line_chart(df['A'])

st.header('3. Area Chart')
st.area_chart(df.A)
st.area_chart(df)

st.area_chart(df, y=['A', 'B', 'C'],
              color = ['#ff0033', '#009933', '#000066'])

st.header('4. Scatter plot')
st.scatter_chart(df, x='A', y='B')
st.scatter_chart(df, x='A', y='B', color='C')

df['D'] = np.random.choice(['x','y','z'], size=20)
st.dataframe(df)
st.scatter_chart(df, x='A', y='B', color='C', size='D')

st.header('5. map')
loc = {'강남구청':[37.52579, 127.0483],
        '서초구청':[37.49093, 127.0329],
        '동작구청':[37.51871, 126.9364],
        '구로구청':[37.50237, 126.8890],
        '양천구청' :[37.52007, 126.9549],
        '영등포구청': [37.54240, 126.8402],
        '관악구청': [37.48467, 126.9515],
        '용산구청' :[37.53804, 126.9913],
        '서대문구청': [37.58567, 126.9357],
        '마포구청' : [37.57003, 126.9019],
        '은평구청' : [37.60675, 126.9302],
        '종로구청' : [37.57615, 126.9790],
        '중구청' : [37.56798, 126.9975],
        '성북구청' : [37.59342, 127.0172],
        '동대문구청' : [37.57792, 127.0401],
        '중랑구청' : [37.60961, 127.0931],
        '노원구청' : [37.65664, 127.0559],
        '도봉구청' : [37.67214, 127.0462],
        '강북구청' : [37.64278, 127.0253],
        '광진구청' : [37.54104, 127.0826],
        '강동구청' : [37.53246, 127.1237],
        '송파구청' : [37.51803, 127.105]}

df_loc = pd.DataFrame(loc).T
df_loc.columns = ['lat', 'lon']
st.dataframe(df_loc)

st.map(df_loc, size=30, color='#00ff00', zoom=14)

st.header('6. matplotlib pyplot')
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df.A)
st.pyplot(fig)

fig, ax = plt.subplots()
ax.scatter(df.A, df.B)
ax.set_title('Scatterplot')
ax.set_xlabel('A')
ax.set_ylabel('B')
st.pyplot(fig)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(len(df.A)), df.B)
st.pyplot(fig)

import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.header('지도시각화: folium')

map = folium.Map(location=[37.5666,126.9782],
                 zoom_start=12)
st_folium(map, width=600, height=400)

mc = MarkerCluster().add_to(map)

for gu, pos in loc.items():
    folium.Marker(location=pos,
              popup=folium.Popup(gu, max_width=200)).add_to(mc)
st_folium(map, width=600, height=400)

st.divider()

c1, c2 = st.columns(2)

m1 = folium.Map([37.574, 126.973], zoom_start=9)
m2 = folium.Map([37.574, 126.973], zoom_start=8)

with c1:
    st.subheader('지도1')
    st_folium(m1, key='x')

with c2:
    st.subheader('지도2')
    st_folium(m2, key='y')

st.divider()

st.header('경기도인구데이터 지도시각화')

import json

with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
    geo_gg = json.loads(f.read())

df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')
st.dataframe(df_gg)
st.markdown('2007년 경기도인구데이터')
map = folium.Map(location=[37.5666,126.9782], zoom_start=8)
folium.GeoJson(geo_gg).add_to(map)
folium.Choropleth(geo_data=geo_gg,
                  data=df_gg[2007],
                  columns=[df_gg.index, df_gg[2007]],
                  key_on='feature.properties.name').add_to(map)

st_folium(map, width=600, height=400)
