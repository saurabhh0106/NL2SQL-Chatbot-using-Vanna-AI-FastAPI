from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.vanna_setup import vn

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "NL2SQL Chatbot Running"}

@app.post("/ask")
def ask(request: QueryRequest):
    try:
        sql = vn.generate_sql(request.question)
        result = vn.run_sql(sql)
        return {"question": request.question, "sql": sql, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "OK"}
