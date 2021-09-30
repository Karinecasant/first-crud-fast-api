from app.repositories.schema.post_schema import PostUpdateRepository
from typing import List, Optional

from app.domains import Post


class PostRepository:
    def __init__(self, database: List[Post]):
        self._post_database = database

    def get_by_id(self, post_id: str) -> Optional[Post]:
        found_post = [post for post in self._post_database if post.id == post_id]

        if len(found_post) > 0:
            return found_post[0]

    def create(self, post: Post):
        self._post_database.append(post)

    def get_all(self):
       return self._post_database

    def delete(self, post_id: str):
        if post := self.get_by_id(post_id):
            self._post_database.remove(post)

            return True
        
        return False

    def update(self, post_id:str, post_update_repository: PostUpdateRepository):
        if post := self.get_by_id(post_id):
            post.title = post_update_repository.title
            post.content = post_update_repository.content
            post.published_at = post_update_repository.published_at

            return post
    
    def clear(self):
        self._post_database.clear()
    

