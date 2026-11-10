from repository import BookRepository
from models import Book
from fastapi import FastAPI, HTTPException

app = FastAPI()
book_repository = BookRepository()

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    return book_repository.create(book)

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = book_repository.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/books/", response_model=list[Book])
def get_all_books():
    return book_repository.get_all()

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    updated_book = book_repository.update(book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    deleted_book = book_repository.delete(book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
