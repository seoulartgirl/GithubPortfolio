import streamlit as st

#mysql 연결(접속)
conn = st.connection('shopdb',
              type='sql',
              url='mysql://streamlit:123@localhost:3306/shopdb')

#질의 수행
df = conn.query('SELECT * FROM customer;', ttl=600)

st.write(df)

df.itertuples()
for row in df.itertuples():
    st.write(f'{row.customer_name}이 {row.phone}을 가짐')

sql = '''INSERT INTO customer
 (customer_id, customer_name, phone, birthday) values 
 (6, '홍길동', '010-1111-1111', '2000-01-30');
 '''

with conn.session as s:
    s.execute(sql)