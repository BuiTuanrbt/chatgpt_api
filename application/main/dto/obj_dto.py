from typing import Optional

from pydantic import BaseModel, Field


class HelloDTO(BaseModel):
  msg: Optional[str] = Field(
    None, description='The hello message'
  )
