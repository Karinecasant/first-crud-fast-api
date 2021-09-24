from pydantic import BaseModel

class CreateCommentRequest(BaseModel):
    parent_id: str
    title: str
    author: str
    content: str