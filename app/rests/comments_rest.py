from fastapi import APIRouter, HTTPException, status

from app.rest_api import rest_api

from app.rests.schemas import CreateCommentRequest
from app.businesses.schema import CommentData, UpdateCommentData

comment_router = APIRouter(prefix="/comments")

@comment_router.get('/comments/{comment_id}')
def get_comment(comment_id: str):
   
   if comment := rest_api.comment_business.get_by_id(comment_id):
       return comment

   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@comment_router.post('/comments')
def create_comment(create_comment: CreateCommentRequest):
    comment_data = CommentData(**create_comment.dict())

    return rest_api.comment_business.create(comment_data)


@comment_router.put('/{comment_id}')
def update_post(comment_id: str, newcomment: UpdateCommentData):
    if updated_comment := rest_api.comment_business.update(comment_id, newcomment):
        return updated_comment

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)


@comment_router.delete('/comments/{comment_id}')
def delete_comment(comment_id: str):
    if not rest_api.comment_business.delete(comment_id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

