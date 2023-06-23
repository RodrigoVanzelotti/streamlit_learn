import streamlit as st
import yfinance as yf

ticker = 'PETR4.SA'
data = yf.Ticker(ticker)

df = data.history(period='1d', start='2012-6-1', end='2023-6-22')

st.title('App em 1 minuto')

st.text('''
Texto que explica o dataframe e todas suas nuancias
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
''')

st.write('#### Preço de Fechamento')
st.line_chart(df.Close)
st.write('#### Preço de Volume')
st.line_chart(df.Volume)
st.snow()