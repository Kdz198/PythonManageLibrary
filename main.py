from fastapi import FastAPI
from routers import BookRouter

app = FastAPI(
    title="Library Management API",
    description="Đây là API Quản lý Thư viện do tôi học chuyển chuyển từ Spring Boot sang.",
    version="1.0.0",
    contact={
        "name": "Khang",
        "email": "khang@example.com",
    }
)

#Inject Router vào mainController
app.include_router( BookRouter.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
