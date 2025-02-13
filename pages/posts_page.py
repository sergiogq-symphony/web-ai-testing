from typing import List
from pydantic import BaseModel

# Define the output format as a Pydantic model
class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int


class Posts(BaseModel):
	posts: List[Post]
