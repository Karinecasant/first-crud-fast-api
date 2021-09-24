from fastapi import APIRouter, Response, status, HTTPException

from app.repositories import PostRepository

from app.businesses import PostBusiness
from app.businesses.schema import PostData, UpdatePostData

from .schemas import CreatePostRequest

post_router = APIRouter(prefix="/posts")

post_repository = PostRepository([])
post_business = PostBusiness(post_repository)

@post_router.get('/{post_id}')
def get_post(response: Response, post_id: str):
   post = post_business.get_by_id(post_id)

   if post is not None:
       return post
    
   response.status_code = status.HTTP_404_NOT_FOUND

@post_router.post('')
def create_post(body: CreatePostRequest):
    post_data = PostData(**body.dict())

    return post_business.create(post_data)

@post_router.get('')
def get_posts():
    return post_business.get_all()

@post_router.put('/{post_id}')
def update_post(post_id: str, newpost: UpdatePostData):
    if updated_post := post_business.update(post_id, newpost):
        return updated_post

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

@post_router.delete('/{post_id}')
def delete_post(post_id: str):
    if not post_business.delete(post_id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    
