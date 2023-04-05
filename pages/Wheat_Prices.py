import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wheat Charts", page_icon="🌾")


st.title("Cash Prices")
st.write("Below is the cash price for wheat in different strands in different parts of the state. Select the region and strand you are interested in and the table and the chart will adjust to your input. This data is separated into rows by week of the year. In many areas and strands there is no information recorded, but for every week there should be an aggregate value for referance")


df= pd.read_csv('https://raw.githubusercontent.com/Lusk27/app_display/main/Data/FULL_CASH.csv')

#st.download_button("Download Data", df)
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

#METRIC = st.selectbox(
#    'Metric',
#    ("Max","Min","Average","Median","Standard Deviation")
#)

METRIC = st.multiselect('Select One or Many',
['Average','Median', 'Max', 'Min', 'Standard Deviation'],
['Median']
)

st.subheader('Charted over the Year')
st.write("Seelct which metrics you want to see, you can select multiple")

chart = df_pivot[METRIC]


st.line_chart(data=chart)

def link_to_github():
    href = '<a href="https://github.com/Lusk27/app_display/tree/main/Data" target="_blank">Link to GitHub</a>'
    return href

st.markdown(link_to_github(), unsafe_allow_html=True)