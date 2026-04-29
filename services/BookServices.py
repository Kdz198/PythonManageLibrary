from fastapi import HTTPException

from schemas.BookDTO import BookDTO

fakeDb: list[BookDTO] = [
    BookDTO(id=1, title="Sói Già Phố Wall", author="Jordan Belfort", yearPublished=2007),
    BookDTO(id=2, title="Đắc Nhân Tâm", author="Dale Carnegie", yearPublished=1936),
    BookDTO(id=3, title="Sạch Mã (Clean Code)", author="Robert C. Martin", yearPublished=2008),
    BookDTO(id=4, title="Người Giàu Nhất Thành Babylon", author="George S. Clason", yearPublished=1926),
    BookDTO(id=5, title="Nhà Giả Kim", author="Paulo Coelho", yearPublished=1988),
]

def getAllBooks():
    return fakeDb


def createBook(book: BookDTO) -> BookDTO:
    fakeDb.append(book)
    return book

def getById (bookId: int) -> BookDTO:
    for book in fakeDb:

        if book.id == bookId:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

def updateBook(bookId: int, updatedBook: BookDTO) -> BookDTO:

    # hàm enumerate là vừa for each vừa for i, nó sẽ trả về cả index và giá trị của phần tử trong list
    for index, book in enumerate(fakeDb):
        if book.id == bookId:
            fakeDb[index] = updatedBook
            return updatedBook

    raise HTTPException(status_code=404, detail="Book not found")

def deleteBook(bookId: int):

    for index, book in enumerate(fakeDb):
        if book.id == bookId:
          fakeDb.pop(index)
          return {"message": "Book deleted successfully"}

    raise HTTPException(status_code=404, detail="Book not found")

def deleteAllBooks():
    fakeDb.clear()
    return {"message": "All books deleted successfully"}