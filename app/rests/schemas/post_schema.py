from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    title: str
    author: str
    content: str