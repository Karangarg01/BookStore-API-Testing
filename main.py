from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dummy database
books_db = {
    "1": {"title": "1984", "author": "George Orwell"},
    "2": {"title": "The Alchemist", "author": "Paulo Coelho"}
}

users_db = {
    "test_user": "test_pass"
}

tokens = {}

class LoginRequest(BaseModel):
    username: str
    password: str

class OrderRequest(BaseModel):
    book_id: str
    token: str

@app.post("/login")
def login(req: LoginRequest):
    if users_db.get(req.username) == req.password:
        token = f"token_{req.username}"
        tokens[token] = req.username
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/books")
def get_books():
    return books_db

@app.post("/order")
def order_book(order: OrderRequest):
    if order.token not in tokens:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if order.book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book '{books_db[order.book_id]['title']}' ordered successfully"}

@app.delete("/book/{book_id}")
def delete_book(book_id: str, token: str):
    if token not in tokens:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
    return {"message": f"Book with id {book_id} deleted"}