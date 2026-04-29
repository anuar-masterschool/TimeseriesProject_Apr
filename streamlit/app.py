import streamlit as st
import pandas as pd


st.write("# title")
st.write("## Subtitle")
a = 3
b = 7
c = a + b

st.write(c)

dog_age = int(st.text_input("Enter the age of your dog: "))

dogs_human_age = dog_age*7

st.write(dogs_human_age)

if dog_age > 7:
    with st.chat_message("user"):
        st.write("Hello, how are you?")

if st.button("Show pop‑up"):
    st.toast("This is a pop‑up message!", icon="🎉")

values = st.multiselect("Choose your favorite fruits:",
                        ["Apple", "Banana", "Orange", "Grapes", "Mango", "Strawberry"])


for fruit in values:
    st.write(f"Uuu {fruit} is a nice choice")

df = pd.read_csv("streamlit/data_daily.csv")

st.write(df)

st.line_chart(df["Receipt_Count"])

d = st.date_input("When's your birthday")
st.write("Your birthday is:", d)



col1, col2 = st.columns(2)

with col1:
    a = st.text_input("sdf")

with col2:
    st.write(df)

with st.sidebar:
    st.write(df)

    st.line_chart(df["Receipt_Count"])

    d = st.date_input("When's your birthday")
    st.write("Your birthday is:", d)
