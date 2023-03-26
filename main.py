from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"title": "Mew", "content": "Mewing", "id": 1}, {
    "title": "favorite food", "content": "Samosa", "id": 2}]


@app.get("/")
async def root():
    return {"message": "Hello You"}


@app.get("/posts")
async def get_posts():
    return {"data": my_post}


@app.post("/posts")
async def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
