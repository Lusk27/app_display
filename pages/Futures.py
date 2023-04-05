import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
st.title('Futures')

df= pd.read_csv('https://raw.githubusercontent.com/BYUIDSconsulting/agecon_slade_fa22/master/personal_folders/trey_lusk/Data/Future_O_Wheat_real.csv?token=GHSAT0AAAAAAB5X2LK22HHECHVSCPAPVFXIZBMXI6Q')

ATTRIBUTE = st.selectbox(
    'Select a Type',
    ("W1_Comdty","KW!_Comdty","MW1_Comdty"))

Truth=df.query('Attribute == @ATTRIBUTE')

future_pivot = Truth.pivot(index='Week', columns=['Year', 'Attribute'], values='Value')
future_pivot['Average'] = future_pivot.mean(axis=1)
future_pivot['Median'] = future_pivot.median(axis=1)
future_pivot['Max'] = future_pivot.max(axis=1)
future_pivot['Min'] = future_pivot.min(axis=1)
future_pivot['Standard Deviation'] = future_pivot.std(axis=1)
st.dataframe(future_pivot)

METRIC = st.multiselect('Select One or Many',
['Average','Median', 'Max', 'Min', 'Standard Deviation'],
['Median']
)

chart = future_pivot[METRIC]
st.subheader('Charted over the Year')
st.write("Seelct which metrics you want to see, you can select multiple")


st.line_chart(data=chart)

