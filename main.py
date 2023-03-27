from random import randrange
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
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_post.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Here is the post {id}"}
