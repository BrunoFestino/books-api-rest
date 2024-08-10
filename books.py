from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [ {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

#Getting all the books
@app.get("/books")
async def read_all_books():
    return BOOKS 

#Getting my favourite book
@app.get("/books/mybook")
async def read_all_books():
    return{"book_title":"My favourite book"}


#Getting a dynamic book
@app.get("/books/{book_tittle}")
async def read_books(book_tittle: str):
    for book in BOOKS:
        if book.get("title").casefold()== book_tittle.casefold():
            return book
        
#Using query parameter
@app.get("/books/")
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold()== category.casefold():
            books_to_return.append(book)
    return books_to_return


#Getting book by book author
@app.get("/book/{book_author}/")
def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
    
@app.post("/books/create_book")
def create_book(new_book=Body()):
    BOOKS.append(new_book)