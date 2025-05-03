from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    state: str
    pin_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    user: User
    content: str
    replies: Optional[List['Comment']] = None # Recursive reference to allow nested comments

    # created_at: str
    # updated_at: str
    # is_deleted: bool = False
    # is_deleted_at: Optional[str] = None
    # is_deleted_by: Optional[User] = None
    # is_edited: bool = False
    # is_edited_at: Optional[str] = None
    # is_edited_by: Optional[User] = None
    # is_pinned: bool = False
    # is_pinned_at: Optional[str] = None
    # is_pinned_by: Optional[str] = None

Comment.model_rebuild()  # Rebuild the model to resolve forward references

address = Address(
    street="123 Harban Singh Marg",
    city="New Delhi",
    state="Delhi",
    pin_code="110019"
)

user = User(
    id=1,
    name="Sourabh Kumar",
    address=address
)

comment = Comment(
    id = 1,
    user = user,
    content = "First comment",
    replies = [
        Comment(
            id = 2,
            user = user,
            content = "First reply",
        ),
        Comment(
            id = 3,
            user = user,
            content = "Second reply",
        )
    ]
) 