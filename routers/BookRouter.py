from typing import Any, Coroutine, List

from fastapi import APIRouter

from schemas.BookDTO import BookDTO

from services import BookServices

# Khởi tạo Router, tương đương @RestController + @RequestMapping("/books")
router = APIRouter(
    prefix="/books", tags=["Books"]
)

@router.post("/")
async def createBook(book: BookDTO):
    return BookServices.createBook(book)


@router.get("/")
async def getAllBooks() -> List[BookDTO]:
    return BookServices.getAllBooks()

@router.get("/{id}")
async def getBook(id: int) -> BookDTO:
    return BookServices.getById(id)

@router.put("/{id}")
async def updateBook(id: int, book: BookDTO) -> BookDTO:
    return BookServices.updateBook(id, book)

@router.delete("/{id}")
async def deleteBook(id: int) -> Any:
    return BookServices.deleteBook(id)