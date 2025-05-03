from pydantic import BaseModel  # type: ignore
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int 
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    tags: List[str]
    published: bool = False
    image_url: Optional[str] = None    