from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres123")
DB_NAME = os.getenv("DB_NAME", "meubanco")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

@app.get("/")
def root():
    return {"message": "CI/CD funcionando, top demais!"}

@app.get("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASS,
            dbname=DB_NAME,
            host=f"/cloudsql/{INSTANCE_CONNECTION_NAME}"
        )
        conn.close()
        return {"status": "Conectou no banco com sucesso!"}
    except Exception as e:
        return {"erro": str(e)}

