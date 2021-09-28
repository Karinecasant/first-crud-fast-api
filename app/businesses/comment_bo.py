from uuid import uuid4
from typing import Optional
from datetime import datetime

from app.domains import Comment

from app.repositories import CommentRepository, PostRepository
from app.repositories.schema import CommentUpdateRepository

from .schema import CommentData, UpdateCommentData

class CommentBusiness:
    def __init__(self, comment_repository: CommentRepository, post_repository: PostRepository):
        self._comment_repository = comment_repository
        self._post_repository = post_repository

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

        # Só criar o comment no repository se existir
        # um comment ou um post com o id do parent_id

    def update(self, id: str, newcomment: UpdateCommentData):
        update_object: CommentUpdateRepository(
            content=newcomment.content
        )

    def delete(self, id: str):
        return self._comment_repository.delete(id)