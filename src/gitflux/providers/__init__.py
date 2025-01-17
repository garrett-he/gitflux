from abc import ABC, abstractmethod
from typing import Iterable

from gitflux.core.models import Repository


class GitServiceProvider(ABC):
    @abstractmethod
    def get_repos(self) -> Iterable[Repository]:
        ...

    @abstractmethod
    def create_repo(self, name: str, private: bool):
        ...

    @abstractmethod
    def delete_repo(self, name: str):
        ...
