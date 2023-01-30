import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(fruit):
    fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit}")
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title('🥣🥗🐔 This is ma title🥑🍞')
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Banana'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error("Please select a fruit to get information.")

    else:
        new_fruit = get_fruityvice_data(fruit_choice)
        st.dataframe(new_fruit)

except URLError as e:
    st.error()


st.header("The fruit list contains:")
if st.button('Get Fruit Load List'):
        my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
        my_data_rows = get_fruit_load_list()
        st.dataframe(my_data_rows)

def insert_row_snowflake(fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute(f"insert into fruit_load_list values ('{fruit}')")
        return f"Thanks for adding {fruit}"



add_my_fruit = st.text_input('What fruit would you like to add?', 'Kiwi')
if st.button('Add A Fruit To The List'):
        my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
        new_fruit = insert_row_snowflake(add_my_fruit)
        st.dataframe(new_fruit)
