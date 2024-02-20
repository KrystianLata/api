from fastapi import FastAPI
from app.routers import home, page1, page2, page3

app = FastAPI()

app.include_router(home.router)
app.include_router(page1.router, prefix="/page1")
app.include_router(page2.router, prefix="/page2")
app.include_router(page3.router, prefix="/page3")
