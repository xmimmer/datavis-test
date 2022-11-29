import streamlit as st
import pandas as pd 
import numpy as np 
from pathlib import Path 

st.title('Fisse, kusse, Lukas sidder i bur!')

@st.cache
def load_data(nrows):    
    data = pd.read_csv('ds_salaries.csv', nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(607)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
    

#Mean of 'salary_in_usd' based on 'company_size'
salary_mean = data.groupby("company_size")["salary_in_usd"].mean() 
#print(salary_mean)

counts = data["experience_level"].value_counts().sort_index() 
#print(counts)





