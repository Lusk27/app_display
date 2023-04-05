import streamlit as st
import pandas as pd

cash= pd.read_csv('https://raw.githubusercontent.com/Lusk27/app_display/main/Data/FULL_CASH.csv')
future= pd.read_csv('https://raw.githubusercontent.com/Lusk27/app_display/main/Data/Future_O_Wheat_real.csv')

st.title("Basis")
st.write("The Basis is the differnece between the cash price and the future price, so the higher this number the greater advantage for the vender. This Number can be positive or negitive depending if the future is less than or grater than the cash price")

CITY = st.selectbox(
    'Select a City',
    ('Rexburg / Ririe','Idaho Falls','Blackfoot / Pocatello','Grace / Soda Springs','Burley / Rupert','Meridian',
'Nezperce / Craigmont','Nampa / Weiser','Twin Falls / Buhl / Jerome / Wendell','Moscow / Genesee'))

ATTRIBUTE = st.selectbox(
    'Select a Strain',
    ('SWW', 'HRW', 'DNS', 'HWW'))

if ATTRIBUTE == 'SWW':
    FUTURE_TYPE = 'W1_Comdty'
elif ATTRIBUTE == 'HRW':
    FUTURE_TYPE = 'KW!_Comdty'
else:
    FUTURE_TYPE = 'MW1_Comdty'

cash_tb=cash.query('Attribute == @ATTRIBUTE & Location == @CITY')
future_tb=future.query('Attribute == @FUTURE_TYPE')

future_tb['Week']= pd.to_numeric(future_tb['Week'])
future_tb = future_tb.rename(columns={'Value':'future', 'Attribute':'Future_Type'})
cash_tb = cash_tb.rename(columns={'Value': 'cash','Attribute':'Wheat_Type'})
merged_df = concatenated_df = pd.concat([cash_tb.set_index(['Year', 'Week']),
                             future_tb.set_index(['Year', 'Week'])],
                            axis=1)

merged_df['Basis'] = merged_df['cash'] - merged_df['future']
merged_df=merged_df.reset_index()
merged_df = merged_df[merged_df["Location"].notnull()]
basis_pivot = merged_df.pivot(index='Week', columns=['Year', 'Future_Type','Wheat_Type'], values='Basis')
basis_pivot['Average'] = basis_pivot.mean(axis=1)
basis_pivot['Median'] = basis_pivot.median(axis=1)
basis_pivot['Max'] = basis_pivot.max(axis=1)
basis_pivot['Min'] = basis_pivot.min(axis=1)
basis_pivot['Standard Deviation'] = basis_pivot.std(axis=1)
st.dataframe(basis_pivot)

METRIC = st.multiselect('Select One or Many',
['Average','Median', 'Max', 'Min', 'Standard Deviation'],
['Median']
)

chart = basis_pivot[METRIC]
st.subheader('Charted over the Year')
st.write("Seelct which metrics you want to see, you can select multiple")


st.line_chart(data=chart)

mean_value = merged_df['Basis'].mean()
min_value = merged_df['Basis'].min()
max_value = merged_df['Basis'].max()


st.subheader('Compare your Week to the Average')
st.write('For any particular week you can compare it to the total average')

week = st.number_input('Enter a Week (This should be a Number)',min_value=1,step=1)
year = st.selectbox('Select a year:', merged_df['Year'].unique())
# Get the value of the selected week
week_value = merged_df.loc[(merged_df['Week'] == week) & (merged_df['Year'] == year), 'Basis'].values[0]
# Create a bar chart that shows the selected week's value compared to the mean, min, and max
chart_data = pd.DataFrame({'Basis': [week_value, mean_value, min_value, max_value],
                           'category': ['Week Value', 'Mean', 'Min', 'Max']})
st.bar_chart(chart_data.set_index('category'))
