import pandas as pd
import streamlit as st
st.title('Data Analysis')
st.write('Data Analysis on Automobile Data')
#df = pd.read_csv('Automobile.csv')
df = pd.read_csv('https://raw.githubusercontent.com/Jesteena714/my_first_streamlit_app1/refs/heads/main/Automobile.csv')
st.dataframe(df)
st.write('Scatter Plot')
st.scatter_chart(data=df,  x='length', y='mileage', x_label='Length', y_label='Mileage')
st.write('Bar Chart')
st.bar_chart(data=df,  x='length', y='mileage', x_label='Length', y_label='Mileage')
st.write('Line Chart')
st.line_chart(data=df,  x='length', y='mileage', x_label='Length', y_label='Mileage')
st.write('Area Chart')
st.area_chart(data=df,  x='length', y='mileage', x_label='Length', y_label='Mileage')
