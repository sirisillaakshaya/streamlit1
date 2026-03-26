import streamlit as st
st.title("Registration Form")
with st.form("my_form"):
    name1,name2=st.columns(2)
    with name1:
        first_name=st.text_input("First Name")
    with name2:
        last_name=st.text_input("Last Name")
    email=st.text_input("EMail")
    password1=st.text_input("password",type="password")
    password2=st.text_input("confirm password",type="password")
    address=st.text_area("Message")
    submit=st.form_submit_button("Submit")
    if(submit):
        if(password1==password2):
            st.success("Registration suceesfully")
        else:
            st.error("password does not match")

