import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

about_content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae tellus metus. Nullam volutpat rhoncus purus, tincidunt ultricies purus sagittis elementum. Donec interdum ante maximus massa aliquam, eget tempor magna tempus. Vivamus sit amet suscipit massa. Donec in metus elit. Quisque vulputate aliquam ultricies. Vivamus gravida gravida tellus, eget pretium ipsum efficitur vitae. Nam auctor ligula sit amet tellus condimentum, vitae faucibus enim auctor. Pellentesque feugiat molestie orci quis elementum."""
st.write(about_content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
