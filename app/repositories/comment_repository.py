from app.domains import comment
from app.domains.comment import Comment
from app.repositories.schema.comment_schema import CommentUpdateRepository
from typing import List, Optional

from app.domains import Comment


class CommentRepository:
    def __init__(self, database: List[Comment]):
        self._comment_database = database

    def get_by_id(self, id: str) -> Optional[Comment]:
        found_comment = [comment for comment in self._comment_database if comment.id == id]

        if len(found_comment) > 0:
            return found_comment[0]

    def get_all(self):
        return self._comment_database

    def create(self, comment: Comment):
        self._comment_database.append(comment)
        
    def delete(self, comment_id: str):
        if comment := self.get_by_id(comment_id):   # faz a criação e verifica se é nulo
            self._comment_database.remove(comment)

            return True
        
        return False

    def update(self, id:str, comment_update: CommentUpdateRepository):
        if comment := self.get_by_id(id):            # faz a criação e verifica se é nulo
            comment.content = comment_update.content

            return comment

    def clear(self):
        self._comment_database.clear()