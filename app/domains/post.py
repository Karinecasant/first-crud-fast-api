from typing import Optional
from dataclasses import dataclass

@dataclass
class Post:
    id: str
    title: str
    author: str
    content: str
    created_at: str
    published_at: Optional[str]

