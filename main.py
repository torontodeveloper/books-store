from fastapi import FastAPI
import logging


app = FastAPI()
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

BOOKS = [
    {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'category': 'science'},
    {'title': 'The Selfish Gene', 'author': 'Richard Dawkins', 'category': 'science'},
    {'title': 'Sapiens: A Brief History of Humankind', 'author': 'Yuval Noah Harari', 'category': 'history'},
    {'title': 'Fermat’s Enigma', 'author': 'Simon Singh', 'category': 'math'},
    {'title': 'The Joy of x', 'author': 'Steven Strogatz', 'category': 'math'},
    {'title': 'How Not to Be Wrong: The Power of Mathematical Thinking', 'author': 'Jordan Ellenberg', 'category': 'math'}
]

@app.get('/books')
async def read_books():
    logger.debug('THIS IS DEBUG*******************')
    return BOOKS

@app.get('/books/{title}')
async def read_book_title(title):
    logger.debug('THIS IS BOOKS BY TITLE DEBUG*******************')
    for book in BOOKS:
        if book['title']==title:
            return book
        
@app.get('/books-author/{author}')
async def read_book_author(author):
    logger.debug('THIS IS BOOKS BY AUTHOR DEBUG*******************')
    for book in BOOKS:
        if book['author']==author:
            return book