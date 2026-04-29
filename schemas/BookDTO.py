from typing import Optional

from pydantic import BaseModel

 # Kế thừa baseModel để nó có sẵn constructor, getter setter, jsonParse,...
class BookDTO(BaseModel):
    id : int
    title : str
    author: str
    yearPublished : Optional[int] = None
