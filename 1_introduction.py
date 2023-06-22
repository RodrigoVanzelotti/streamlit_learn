# pip install streamlit
# streamlit hello
# mostrar site do streamlit

import streamlit as st

# Escrevemos em markdown
st.write("""
# Começamos no Streamlit!
""")

# para rodar o programa, basta escrever:
# streamlit run introduction.py

# Caso não saiba markdown
# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# Teste utilizando dados reais
st.write("""
Vamos analisar valores da **bolsa da Petrobras**:
""")
import yfinance as yf

ticker = 'PETR4.SA'

data = yf.Ticker(ticker)

df = data.history(period='1d', start='2018-6-1', end='2023-6-22')

st.write('### Preço de Fechamento')
st.line_chart(df.Close)
st.write('### Preço de Volume')
st.line_chart(df.Volume)

