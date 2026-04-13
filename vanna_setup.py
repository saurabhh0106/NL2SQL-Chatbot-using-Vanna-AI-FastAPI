from vanna.openai import OpenAI_Chat
from vanna.chromadb import ChromaDB_VectorStore
from app.config import OPENAI_API_KEY

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self):
        ChromaDB_VectorStore.__init__(self)
        OpenAI_Chat.__init__(self, api_key=OPENAI_API_KEY)

vn = MyVanna()

vn.connect_to_sqlite("data/sample.db")

vn.train(
    ddl="""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        total_purchase FLOAT
    );
    """
)

vn.train(
    question="Top 5 customers by purchase",
    sql="SELECT * FROM customers ORDER BY total_purchase DESC LIMIT 5;"
)
