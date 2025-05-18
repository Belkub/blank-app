import streamlit as st

st.title('Конвертер валют')
col1, col2 = st.columns(2)
x = col1.number_input('', min_value = 0.0, value = 1.0, step = 1.0)
rates = {'USD':80.35, 'KZT':0.17}
currency = col2.selectbox('Валюта', list(rates))
st.success(f'{x*rates[currency]:,.2f} RUB')
