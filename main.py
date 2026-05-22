from fastapi import FastAPI
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",user="root",database="api_crud",password="Keerthi@425"
)
curser_obj=conn_obj.cursor(dictionary=True)
app=FastAPI() # object of FastAPI

@app.post("/add_worker") #api backend
def add_employee(new_data:dict):
    name=new_data["n"]
    email=new_data["e"]
    dept=new_data["d"]
    query="insert into emp(name,email,department) values(%s,%s,%s)"
    values=(name,email,dept)
    curser_obj.execute(query,values)
    conn_obj.commit()

@app.get("/view")
def view_emp():
    query="select * from emp"
    curser_obj.execute(query)
    return curser_obj.fetchall()    

