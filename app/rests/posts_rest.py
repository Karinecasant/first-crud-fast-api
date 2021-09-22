from fastapi import FastAPI, Response, status, HTTPException

from app.repositories import PostRepository

from app.businesses import PostBusiness
from app.businesses.schema import PostData, UpdatePostData

from .schemas import CreatePostRequest

app = FastAPI()

post_repository = PostRepository([])
post_business = PostBusiness(post_repository)

@app.get('/posts/{post_id}')
def get_post(response: Response, post_id: str):
   post = post_business.get_by_id(post_id)

   if post is not None:
       return post
    
   response.status_code = status.HTTP_404_NOT_FOUND

@app.post('/posts')
def create_post(body: CreatePostRequest):
    post_data = PostData(**body.dict())

    return post_business.create(post_data)

@app.get('/posts')
def get_posts():
    return post_business.get_all()

@app.put('/posts/{post_id}')
def update_post(post_id: str, newpost: UpdatePostData):
    if updated_post := post_business.update(post_id, newpost):
        return updated_post

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    if not post_business.delete(post_id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        

