import streamlit as st
st.set_page_config(
    page_title='MLP',
    page_icon='🕷️'
)
st.title('Main Page')
st.sidebar.success('Pages above')
st.header('Marie Curie',divider=True)
with st.sidebar:
    st.page_link('pages/data.py',label='Home',icon='🏡')
col1, col2 = st.columns(2)
with col1:
    st.image('https://raw.githubusercontent.com/Jesteena714/my_first_streamlit_app1/refs/heads/main/Image.webp', caption='Marie Curie')
with col2:
    st.text('Marie Curie, née Maria Sklodowska, was born in Warsaw on November 7, 1867, the daughter of a secondary-school teacher. She received a general education in local schools and some scientific training from her father. She became involved in a students’ revolutionary organization and found it prudent to leave Warsaw, then in the part of Poland dominated by Russia, for Cracow, which at that time was under Austrian rule. In 1891, she went to Paris to continue her studies at the Sorbonne where she obtained Licenciateships in Physics and the Mathematical Sciences. She met Pierre Curie, Professor in the School of Physics in 1894 and in the following year they were married. She succeeded her husband as Head of the Physics Laboratory at the Sorbonne, gained her Doctor of Science degree in 1903.')

with st.sidebar:
    st.link_button('Know More', 'https://www.nobelprize.org/prizes/physics/1903/marie-curie/biographical/') 
with st.sidebar:
    st.link_button('Analysis','https://myfirstappapp1-vckr4emapxuhqpjh8db8f8.streamlit.app/data')
