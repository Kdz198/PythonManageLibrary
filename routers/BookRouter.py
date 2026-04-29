from typing import Any, Coroutine

from fastapi import APIRouter

from schemas.BookDTO import BookDTO

# Khởi tạo Router, tương đương @RestController + @RequestMapping("/books")
router = APIRouter(
    prefix="/books", tags=["Books"]
)

@router.post("/")
async def createBook(book: BookDTO) -> dict[str, str | None | BookDTO]: # dùng type hinting của python để chỉ rõ hàm này trả về gì
    return {
        "message": "Sách đã được thêm thành công từ Router riêng!",
        "error": None,
        "data": book
    }