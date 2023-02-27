import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

st.set_page_config(page_title="Futures Charts", page_icon="📈")

st.write('This page will have the same infomation from the powerbi page')


df =pd.read_csv('Lusk27/app_display/Data/test.csv')


st.table(df)

#st.bar_chart(data=df, x=Location )