from dataclasses import dataclass

@dataclass
class CommentData:
    parent_id: str
    title: str
    author: str
    content: str

@dataclass
class UpdateCommentData:
    title: str
    content: str


