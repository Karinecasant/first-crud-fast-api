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

    def update(self, post_id:str, title: str, content: str, published_at: str):
        if post := self.get_by_id(post_id):
            post.title = title
            post.content = content
            post.published_at = published_at

            return post
    

