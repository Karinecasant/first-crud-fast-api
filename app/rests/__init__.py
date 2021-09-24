from .posts_rest import post_router
from .comments_rest import comment_router

routers = [post_router, comment_router]