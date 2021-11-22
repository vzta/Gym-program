import streamlit as st
import pandas as pd
import time
st.title("Welcome to my Gym Program")

name=st.text_input("Enter your Name: ")
Age=st.number_input("Enter your Age: ", min_value=0, max_value=100, step=1)
Objective=option = st.selectbox(
   'What is your Objective?: ',
     ('Strength', 'Hypertrophy', 'Fat Loss'))
Alumno = {
  "Name": f"{name}",
  "Age": f"{Age}",
  "Objective": f"{Objective}"
}
if name!="":
    st.markdown(
        f"""
        * Name: {name}
        * Age: {Age}
        * Objective: {Objective}
    """
    )
df=pd.DataFrame(Alumno.items())

st.write(df)

if Objective=="Strength":
    st.write(
        "These are some Strength programs for you:  [link](https://liftvault.com/programs/powerlifting/)")
elif Objective=="Hypertrophy":
    st.write(
        "These are some Hypertrophy programs for you: [link](https://liftvault.com/program_goal/hypertrophy/)"
    )

def body_max_index(Height,weight):

    return (weight/(Height*2))*100




st.subheader("Calculate your Body Max Index: ")
Height = st.number_input("Height in CM:", min_value=50, max_value=220, step=1)
weight = st.number_input("Weight in Kg:", min_value=35, max_value=200, step=1)
if st.button("Calculate!:"):
    res=body_max_index(Height, weight)
    st.write("Your Body max index is: ",res)
