import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wheat Charts", page_icon="🌾")

st.write("This will have the wheat infomation")

CITY = st.selectbox(
    'Select a City',
    ('Rexburg / Ririe','Idaho Falls','Blackfoot / Pocatello','Grace / Soda Springs','Burley / Rupert','Meridian',
'Nezperce / Craigmont','Nampa / Weiser','Twin Falls / Buhl / Jerome / Wendell','Moscow / Genesee'))