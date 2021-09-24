from dataclasses import dataclass

@dataclass
class Comment:
    parent_id: str
    id: str
    author: str
    content: str
    created_at: str
