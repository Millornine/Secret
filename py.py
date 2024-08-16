from datetime import datetime
from fastapi import HTTPException
from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error
from typing import Optional
from pydantic import BaseModel


class newmemmodel(BaseModel):
    m_email: str
    m_password: str
    m_name: str
    
class coursemodel(BaseModel):
    c_id: int
    c_name: str
    c_description: str
    c_price: int
    
class EnrollModel(BaseModel):
    cer_id: int
    m_id: int
    c_id: int
    cer_start: datetime
    cer_expire: datetime
    
def create_connection():
    """ Create a database connection to the MySQL server """
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',          # Replace with your MySQL host
            user='root',      # Replace with your MySQL username
            password='0860981399',  # Replace with your MySQL password
            database='senior'   # Replace with your MySQL database
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None




# Start Container about members

def fetchALL(table_name: str):
    """ Fetch all items from the database """
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM `{table_name}`")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows
    return []


def fetch_DataID(id: int,table_name: str, column: str):
    """ Fetch all items from the database """
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM `{table_name}` WHERE {column}_id = {id}")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows
    return None

def add_Member(data: newmemmodel):
    """ Add a new item to the database """
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO `member` (m_email, m_password, m_name) VALUES (%s, %s, %s)"

        values = (data.m_email, data.m_password, data.m_name)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return cursor.lastrowid
    return None


def add_Course(data: coursemodel):
    """ Add a new item to the database """
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO `course` (c_name, c_description, c_price) VALUES (%s, %s, %s)"
        
        values = (data.c_name, data.c_description, data.c_price)
        cursor.execute(query, values)
        connection.commit()
        last_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return last_id
    
    
def add_Enroll(data: EnrollModel):
    """ Add a new item to the database """
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO `enroll` (m_id, c_id, cer_start, cer_expire) VALUES (%s, %s, %s, %s)"
        
        values = (data.m_id, data.c_id, data.cer_start, data.cer_expire)
        cursor.execute(query, values)
        connection.commit()
        last_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return last_id

def update_member(m_id: int, data: newmemmodel):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
            UPDATE `member`
            SET m_email = %s, m_password = %s, m_name = %s
            WHERE m_id = %s
            """
        values = (data.m_email, data.m_password, data.m_name, m_id)
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount > 0:
            res = True
        else:
            res = False
        cursor.close()
        connection.close()
        return res

def update_course(c_id: int, data: coursemodel):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
            UPDATE `course`
            SET c_name = %s, c_description = %s, c_price = %s
            WHERE c_id = %s
        """
        values = (data.c_name, data.c_description, data.c_price, c_id)
        cursor.execute(query, values)
        connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        connection.close()
        return rows_affected
    
def update_enroll(cer_id: int, data: EnrollModel):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
            UPDATE `enroll`
            SET m_id = %s, c_id = %s, cer_start = %s, cer_expire = %s
            WHERE cer_id = %s
        """
        values = (data.m_id, data.c_id, data.cer_start, data.cer_expire, cer_id)
        cursor.execute(query, values)
        connection.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        connection.close()
        return rows_affected
    return None

def delete_Data(m_id: int,table_name: str, column: str):
    """ Delete a member by ID """
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = f"DELETE FROM `{table_name}` WHERE {column}_id = {m_id}"
        cursor.execute(query)
        connection.commit()
        if cursor.rowcount > 0:
            res = True
        else:
            res = False
        cursor.close()
        connection.close()
        return res

# End Container about members



app = FastAPI()

@app.get("/members")
async def FetchAllMember():
    return fetchALL(table_name="member")

@app.get("/courses")
async def FetchAllCourses():
    return fetchALL(table_name="course")

@app.get("/enrolls")
async def FetchAllCourses():
    return fetchALL(table_name="enroll")

@app.get("/enrolls/member/{m_id}")
async def FetchEnrollMemberID(m_id: int):
    id = fetch_DataID(m_id,"enroll","m")
    if id:
        return id
    else:
        raise HTTPException(status_code=404, detail="404 Not Found")
    
@app.get("/enrolls/course/{c_id}")
async def FetchEnrollCourseID(c_id: int):
    id = fetch_DataID(c_id,"enroll","c")
    if id:
        return id
    else:
        raise HTTPException(status_code=404, detail="404 Not Found")


@app.get("/members/{m_id}")
async def FetchAllMemberID(m_id: int):
    id = fetch_DataID(m_id,"member","m")
    if id:
        return id
    else:
        raise HTTPException(status_code=404, detail="404 Not Found")
    
    
@app.get("/courses/{c_id}")
async def FetchAllCourseID(c_id: int):
    id = fetch_DataID(c_id,"course","c")
    if id:
        return id
    else:
        raise HTTPException(status_code=404, detail="404 Not Found")
        
@app.get("/enrolls/{cer_id}")
async def FetchAllEnrollID(cer_id: int):
    id = fetch_DataID(cer_id,"enroll","cer")
    if id:
        return id
    else:
        raise HTTPException(status_code=404, detail="404 Not Found")
        


@app.post("/members")
async def AddMember(data: newmemmodel):
    member = add_Member(data)
    if member:
        return { "messages": f"Created m_id = {member}"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create member")

@app.post("/courses")
async def AddCourse(data: coursemodel):
    member = add_Course(data)
    if member:
        return { "messages": f"Created c_id = {member}"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create courses")

@app.post("/enrolls")
async def AddEnroll(data: EnrollModel):
    member = add_Enroll(data)
    if member:
        return { "messages": f"Created cer_id = {member}"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create enrolls")


@app.put("/members/{m_id}")
async def UpdateMemberID(m_id: int, data: newmemmodel):
    update = update_member(m_id, data)
    if update:
        return {"message": "Member updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Member not found or failed to update")
    
    
@app.put("/courses/{c_id}")
async def UpdateCourseID(c_id: int, data: coursemodel):
    update = update_course(c_id, data)
    if update:
        return {"message": "Course updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Course not found or failed to update")

@app.put("/enrolls/{cer_id}")
async def UpdateEnrollID(cer_id: int, data: EnrollModel):
    update = update_enroll(cer_id, data)
    if update:
        return {"message": "Enroll updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Enroll not found or failed to update")


@app.delete("/members/{m_id}")
async def deleteMemberID(m_id: int):
    delete = delete_Data(m_id,"member","m")
    if delete:
        return {"message": f"Member delete ID: {m_id} successfully"}
    else:
        raise HTTPException(status_code=404, detail="Member not found or failed to delete")

@app.delete("/courses/{c_id}")
async def deleteMemberID(c_id: int):
    delete = delete_Data(c_id,"course","c")
    if delete:
        return {"message": f"Courses delete ID: {c_id} successfully"}
    else:
        raise HTTPException(status_code=404, detail="Courses not found or failed to delete")


@app.delete("/enrolls/{cer_id}")
async def deleteMemberID(cer_id: int):
    delete = delete_Data(cer_id,"enroll","cer")
    if delete:
        return {"message": f"Courses delete ID: {cer_id} successfully"}
    else:
        raise HTTPException(status_code=404, detail="Courses not found or failed to delete")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
