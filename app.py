import streamlit as st

st.title('MY FIRST APP')
st.header('This is Header')
st.subheader('This is Subheader')
st.write('This is normal text!')

name = st.text_input('Enter your name :')
age = st.number_input('Enter your age :', min_value=0, max_value=100, value=18)
skills = st.multiselect('Select your skills :', ['Python', 'Java', 'C++', 'JavaScript'])
field = st.selectbox('Select your field :', ['Data Science', 'Web Development', 'Mobile Development'])

if st.button('Submit'):
    st.success(f'Hello {name}, you are {age} years old and your skills are {", ".join(skills)} in {field} field!')

