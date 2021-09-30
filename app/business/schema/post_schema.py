from dataclasses import dataclass

@dataclass
class PostData:
    title: str
    author: str
    content: str

@dataclass
class UpdatePostData:
    title: str
    content: str
    published_at:str 

