import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import json
from utils.map import load_data, load_geo_json, load_excel_data, draw_mpa

st.divider()
st.header('3. 연도별 인구수에 대한 지도시각화 - 2007년, 2015년, 2019년 연도를 탭으로 제시')

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