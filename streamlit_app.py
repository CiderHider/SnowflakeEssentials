import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title('🥣🥗🐔 This is ma title🥑🍞')
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

# Let's put a pick list here so they can pick the fruit they want to include
st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Banana'])

# Display the table on the page.
st.dataframe(my_fruit_list)
