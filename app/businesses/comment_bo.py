from app.businesses.schema.comment_schema import CommentData, UpdateCommentData
from app.repositories.comment_repository import CommentRepository
from uuid import uuid4
from typing import List, Optional
from datetime import datetime

from app.domains import Comment, comment
from app.repositories import CommentRepositor
from app.repositories.schema import CommentUpdateRepository

from .schema import PostData, UpdatePostData

class CommentBusiness:
    def __init__(self, comment_repository: CommentRepository):
        self._comment_repository = comment_repository

    def get_by_id(self, id: str) -> Optional[Comment]:
        return self._comment_repository.get_by_id(id)

    def create(self, comment_data: CommentData) -> Comment:
        comment = Comment(
            id=str(uuid4()),
            parent_id=comment_data.parent_id,
            author=comment_data.author,
            content=comment_data.content,
            created_at=str(datetime.now()),
        )

    def update(self, id: str, newcomment: UpdateCommentData):
        update_object: CommentUpdateRepository(
            content=newcomment.content
      )

    def delete(self, id: str):
        return self._comment_repository.delete(id)