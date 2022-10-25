import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('Califorlia Housing Data(1990) by Xiaoman Li')
df = pd.read_csv('housing.csv')

# 筛选：house-price、       location、      house-value、    income-level
##'median_house_value''ocean_proximity''median_house_value''median_income'
##     price_filter    location_filter     price_filter     income_filter

# 创建一个从0-500001的滑块用于筛选price
price_filter = st.slider('maximal Median House Price', 0, 500001, 200000) 
df = df[df.median_house_value <= price_filter]


# 创建多选框用于筛选location
location_filter = st.sidebar.multiselect(
     'Choose the Location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults
df = df[df.ocean_proximity.isin(location_filter)]


# 创建单选框用于筛选income
income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High')
)

if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
if income_filter == 'Medium':
    df = df[df.median_income <= 4.5]
if income_filter == 'High':
    df = df[df.median_income > 4.5]

# show on map
st.subheader('See more filterrs in the sidebar:')
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(8, 6))
df.median_house_value.hist(bins=30)
st.pyplot(fig)
