from uuid import uuid4
from typing import Optional
from datetime import datetime

from app.domains import Comment, comment

from app.repositories import CommentRepository, PostRepository
from app.repositories.schema import CommentUpdateRepository

from .schema import CommentData, UpdateCommentData

class CommentBusiness:
    def __init__(self, comment_repository: CommentRepository, post_repository: PostRepository):
        self._comment_repository = comment_repository
        self._post_repository = post_repository

    def get_by_id(self, id: str) -> Optional[Comment]:
        return self._comment_repository.get_by_id(id)

    def get_all(self):
        return self._comment_repository.get_all()

    def create(self, comment_data: CommentData) -> Comment:
        comment_exists = self._comment_repository.get_by_id(comment_data.parent_id)
        post_exists = self._post_repository.get_by_id(comment_data.parent_id)

        if comment_exists or post_exists:
            comment = Comment(
            id=str(uuid4()),
            parent_id=comment_data.parent_id,
            author=comment_data.author,
            content=comment_data.content,
            created_at=str(datetime.now()))
            
            return self._comment_repository.create(comment)

        raise ValueError("Não existe comment para esse parent_id")
        # Só criar o comment no repository se existir
        # um comment ou um post com o id do parent_id

    def update(self, id: str, newcomment: UpdateCommentData):
        update_object = CommentUpdateRepository(
            content=newcomment.content
        )
        return self._comment_repository.update(id, update_object)

    def delete(self, id: str):
        return self._comment_repository.delete(id)