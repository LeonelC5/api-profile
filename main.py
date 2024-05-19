from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "44.194.2.9"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "db_profile_api"  


# Get all profiles
@app.get("/profile")
def get_profiles():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM profile")
    result = cursor.fetchall()
    mydb.close()
    return {"profiles": result}

# Get an profile by ID
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
    name: str
    apellido: str
    correo: str
    password: str
    celular: str
    description: str
    imagen: str
    cursor = mydb.cursor()
    sql = "INSERT INTO profiles (name, apellido, correo, password, celular, description, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, apellido, correo, password, celular, description, imagen)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "profile added successfully"}

# Modify an profile
@app.put("/profile/{id}")
def update_profile(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    name: str
    apellido: str
    correo: str
    password: str
    celular: str
    description: str
    imagen: str
    cursor = mydb.cursor()
    sql = "UPDATE profiles set name=%s, apellido=%s,correo=%s, password=%s, celular=%s, description=%s, imagen=%s  where id=%s"
    val = (name, apellido, correo, password, celular, description, imagen, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "profile modified successfully"}

# Delete an profile by ID
@app.delete("/profile/{id}")
def delete_profile(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM profile WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "profile deleted successfully"}