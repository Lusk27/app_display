import streamlit as st
import pandas as pd

cash= pd.read_csv('https://raw.githubusercontent.com/BYUIDSconsulting/agecon_slade_fa22/master/personal_folders/trey_lusk/Data/FULL_CASH.csv?token=GHSAT0AAAAAAB5X2LK3UL63Y7VP2DTH3OC4ZBMUNPQ')
future= pd.read_csv('https://raw.githubusercontent.com/BYUIDSconsulting/agecon_slade_fa22/master/personal_folders/trey_lusk/Data/Future_O_Wheat_real.csv?token=GHSAT0AAAAAAB5X2LK2OAUDTXCFPF2PO73EZBMUQJA')

FUTURE_TYPE = st.selectbox(
    'Select a Type of Future',
    ("W1_Comdty","KW!_Comdty","MW1_Comdty"))

CITY = st.selectbox(
    'Select a City',
    ('Rexburg / Ririe','Idaho Falls','Blackfoot / Pocatello','Grace / Soda Springs','Burley / Rupert','Meridian',
'Nezperce / Craigmont','Nampa / Weiser','Twin Falls / Buhl / Jerome / Wendell','Moscow / Genesee'))

ATTRIBUTE = st.selectbox(
    'Select a Strain',
    ('Barley_Feed', 'Malting', 'SWW', 'HRW', 'DNS', 'HWW'))

cash_tb=cash.query('Attribute == @ATTRIBUTE & Location == @CITY')
future_tb=future.query('Attribute == @FUTURE_TYPE')

future_tb['Week']= pd.to_numeric(future_tb['Week'])
future_tb = future_tb.rename(columns={'Value': 'future'})
cash_tb = cash_tb.rename(columns={'Value': 'cash'})
merged_df = concatenated_df = pd.concat([cash_tb.set_index(['Year', 'Week']),
                             future_tb.set_index(['Year', 'Week'])],
                            axis=1)

merged_df['Basis'] = merged_df['cash'] - merged_df['future']

df_pivot = merged_df.pivot(index='Week', columns=['Year', 'Attribute', 'Location'], values='Value')
df_pivot['Average'] = df_pivot.mean(axis=1)
df_pivot['Median'] = df_pivot.median(axis=1)
df_pivot['Max'] = df_pivot.max(axis=1)
df_pivot['Min'] = df_pivot.min(axis=1)
df_pivot['Standard Deviation'] = df_pivot.std(axis=1)

st.dataframe(df_pivot)