pip install fastapi uvicorn mysql-connector-python

from fastapi import FastAPI, HTTPException
import mysql.connector
from mysql.connector import Error

app = FastAPI()

db_config = {
    "host": "localhost",
    "user": siddhesh tawde,
    "password": "siddheshtawde01",
    "database": "tsiddhesh"
}

def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.post("/order")
async def create_order(customer_id: int, item: str, quantity: int):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Insert a new order into the database
            cursor.execute(
                "INSERT INTO orders (customer_id, item, quantity) VALUES (%s, %s, %s)",
                (customer_id, item, quantity),
            )
            connection.commit()
            return {"message": "Order created successfully"}
        except Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            cursor.close()
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Failed to connect to the database")
