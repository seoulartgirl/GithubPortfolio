import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    database = 'shopDB',
    user = 'streamlit',
    pasword = '1234'
)

if conn.is_connected():
    db_info = conn.get_server_info()
    st.write('server_version : ', db_info)

cur = conn.cursor()
cur.execute('SELECT * FROM customer;')

records = cur.fetchall()
st.write(records)

st.write(pd.DataFrame(records, columns = ['id', 'name', 'phone', 'birth']))

def make_df(records):
    return pd.DataFrame(records, columns = ['id', 'name', 'phone', 'birth'])