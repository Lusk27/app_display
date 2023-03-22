import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wheat Charts", page_icon="🌾")

st.write("This will have the wheat infomation")
df= pd.read_csv('/Users/luskenterprises/consulting/app_display/Data/wheat_prices.csv')
CITY = st.selectbox(
    'Select a City',
    ('Rexburg / Ririe','Idaho Falls','Blackfoot / Pocatello','Grace / Soda Springs','Burley / Rupert','Meridian',
'Nezperce / Craigmont','Nampa / Weiser','Twin Falls / Buhl / Jerome / Wendell','Moscow / Genesee'))


ATTRIBUTE = st.selectbox(
    'Select a Strain',
    ('Barley_Feed', 'Malting', 'SWW', 'HRW', 'DNS', 'HWW'))


wheat_table=df.query('Attribute == @ATTRIBUTE & Location == @CITY')

df_pivot = wheat_table.pivot(index='Week', columns=['Year', 'Attribute', 'Location'], values='Value')
df_pivot['Average'] = df_pivot.mean(axis=1)
df_pivot['Median'] = df_pivot.median(axis=1)
df_pivot['Max'] = df_pivot.max(axis=1)
df_pivot['Min'] = df_pivot.min(axis=1)
df_pivot['Standard Deviation'] = df_pivot.std(axis=1)

st.dataframe(df_pivot)

YEAR = st.selectbox(
    'Select a Year',
    (2016.0,2017.0,2018.0,2019.0,2020.0,2021.0,2022.0,2023.0)
)
chart = df.query('Year == @YEAR')
st.line_chart(data=chart, y='Value', x="Week")