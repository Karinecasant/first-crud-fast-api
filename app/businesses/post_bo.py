from uuid import uuid4
from typing import List, Optional
from datetime import datetime

from app.domains import Post
from app.repositories import PostRepository

from .schema import PostData, UpdatePostData


class PostBusiness:
    def __init__(self, post_repository: PostRepository):
        self._post_repository = post_repository

    def get_by_id(self, id: str) -> Optional[Post]:
        return self._post_repository.get_by_id(id)
    
    def get_all(self) -> List[Post]:
        return self._post_repository.get_all()

    def create(self, post_data: PostData) -> Post:
        post = Post(
            id=str(uuid4()),
            title=post_data.title,
            author=post_data.author,
            content=post_data.content,
            created_at=str(datetime.now()),
            published_at=None
        )

        self._post_repository.create(post)

        return post

    def update(self, post_id: str, newpost: UpdatePostData):
        return self._post_repository.update(post_id, newpost.title, newpost.content, newpost.published_at)

    def delete(self, post_id: str):
        return self._post_repository.delete(post_id)


        











