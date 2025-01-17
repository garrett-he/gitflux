from typing import Literal

from pydantic import BaseModel


class Profile(BaseModel):
    provider: Literal['github', 'gitee']
    access_token: str


class Repository(BaseModel):
    name: str
    full_name: str

    def get_prefix(self) -> str:
        return self.full_name[0:self.full_name.index('/')]
