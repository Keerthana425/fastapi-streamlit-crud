import streamlit as st
import requests 
import pandas as pd
server_loc="http://127.0.0.1:8000"

st.title("CRUD operations")

page = st.sidebar.selectbox("Choose operation--", ["add_employee", "view_employees", "update_employee", "delete_employee"])

if page=="add_employee":
   st.header("adding employee")
   with st.form("adding"):
      name=st.text_input("Name")
      email=st.text_input("Email")
      dept=st.selectbox("department : --",["","dev","test","aws","devops","ai/ml engineer","gen-ai"])
      btn=st.form_submit_button("Add Employee")
      if btn:
         new_data={"n":name,"e":email,"d":dept}
         requests.post(f"{server_loc}/add_worker",json=new_data)
   
elif page=="view_employees":
   st.header("viewing employees")
   view_btn=st.button("view")
   if view_btn:
      res=requests.get(f"{server_loc}/view")
      pd_data=pd.DataFrame(res.json(),columns=["id","name","email","department"])
      st.dataframe(pd_data)

elif page=="update_employee":
   st.header("updating employee")
elif page=="delete_employee":
   st.header("deleting employee")