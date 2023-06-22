import streamlit as st
import yfinance as yf

ticker = 'PETR4.SA'
data = yf.Ticker(ticker)

df = data.history(period='1d', start='2018-6-1', end='2023-6-22')

st.title('App em 1 minuto')

st.write('#### Preço de Fechamento')
st.line_chart(df.Close)
st.write('#### Preço de Volume')
st.line_chart(df.Volume)