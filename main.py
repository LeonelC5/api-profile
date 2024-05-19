from fastapi import FastAPI
import mysql.connector
import schemas
import os

app = FastAPI()

host_name = os.environ.get("database-proyecto.c45ddxrq8nnm.us-east-1.rds.amazonaws.com")
port_number = os.environ.get("3306")
user_name = os.environ.get("admin")
password_db = os.environ.get("database-proyecto")
database_name = os.environ.get("db_profile")

# Get all profiles
@app.get("/profile")
def get_profiles():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM profile")
    result = cursor.fetchall()
    mydb.close()
    return {"profiles": result}

# Get a profile by ID
@app.get("/profile/{id}")
def get_profile(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM profile WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"profile": result}

# Add a new profile
@app.post("/profile")
def add_profile(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    sql = "INSERT INTO profiles (nombre, apellido, correo, password, celular, description, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (item.nombre, item.apellido, item.correo, item.password, item.celular, item.description, item.imagen)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "profile added successfully"}

# Modify a profile
@app.put("/profile/{id}")
def update_profile(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    sql = "UPDATE profiles set nombre=%s, apellido=%s,correo=%s, password=%s, celular=%s, description=%s, imagen=%s  where id=%s"
    val = (item.nombre, item.apellido, item.correo, item.password, item.celular, item.description, item.imagen, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "profile modified successfully"}

# Delete a profile by ID
@app.delete("/profile/{id}")
def delete_profile(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM profile WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "profile deleted successfully"}
