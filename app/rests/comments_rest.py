from app.rests.schemas.comment_schema import CreateCommentRequest
from app.businesses.schema.comment_schema import CommentData, UpdateCommentData
from app.repositories import CommentRepository
from app.businesses import CommentBusiness
from fastapi import APIRouter, HTTPException, Response, status

comment_router = APIRouter(prefix="/comments")

comment_repository = CommentRepository([])
comment_business = CommentBusiness(comment_repository)

@comment_router.get('/comments/{comment_id}')
def get_comment(response: Response, comment_id: str):
   comment = comment_business.get_by_id(comment_id)
   
   if comment:
       return comment
   response.status_code = status.HTTP_404_NOT_FOUND

@comment_router.post('/comments')
def create_comment(response: Response, create_comment: CreateCommentRequest):
    comment_data = CommentData(**create_comment.dict())
    return comment_business.create(comment_data)


@comment_router.put('/{comment_id}')
def update_post(comment_id: str, newcomment: UpdateCommentData):
    if updated_comment := comment_business.update(comment_id, newcomment):
        return updated_comment

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)


@comment_router.delete('/comments/{comment_id}')
def delete_comment(comment_id: str):
    if not comment_business.delete(comment_id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

