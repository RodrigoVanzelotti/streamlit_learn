import streamlit as st

# Aqui aprenderemos elementos de texto, todo autoexplicados
# Reforçar a possibilidade de revisão de markdown

st.title('Text Elements')
st.subheader('Esse é o nosso subheader')
st.header('Diferença pequena em relação ao sub (tamanho)')

st.write('''Para textos como html.P
- bullet points só funcionam no write
- Em geral, markdown só funciona no write (e na função de markdown)
''')

st.markdown('''
**utilizando markdown dessa vez**, *entenderam?*

> Isso por exemplo é um blockquote

- **Ponto 1**
- *Ponto 2*
- Ponto 3

[isso aqui é um link pra Asimov Academy](https://hub.asimov.academy)

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

''')

st.text('''
Esse componente pode ser utilizado como um parágrafo
Note que até a fonte é alterada!
- Para escritas maiores
- Para textos de fato
- Eu usei bullet points da maneira errada;
- Só pra exemplificar 
''')

