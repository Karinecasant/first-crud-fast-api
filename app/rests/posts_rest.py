from fastapi import APIRouter, status, HTTPException

from app.rest_api import rest_api

from app.business.schema import PostData, UpdatePostData

from .schemas import CreatePostRequest

post_router = APIRouter(prefix="/posts")


@post_router.get('/{post_id}')
def get_post(post_id: str):
   if post := rest_api.post_business.get_by_id(post_id):
       return post

   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@post_router.post('')
def create_post(body: CreatePostRequest):
    post_data = PostData(**body.dict())

    return rest_api.post_business.create(post_data)

@post_router.get('')
def get_posts():
    return rest_api.post_business.get_all()

@post_router.put('/{post_id}')
def update_post(post_id: str, newpost: UpdatePostData):
    if updated_post := rest_api.post_business.update(post_id, newpost):
        return updated_post

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

@post_router.delete('/{post_id}')
def delete_post(post_id: str):
    if not rest_api.post_business.delete(post_id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    
