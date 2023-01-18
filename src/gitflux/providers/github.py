from __future__ import annotations
from typing import Iterable
from github import Github, AuthenticatedUser, Repository as GitHubRepository
from gitflux.typing import Repository
from gitflux.providers import GitServiceProvider


def create_provider(token: str) -> GitHubService:
    return GitHubService(token=token)


def convert_git_repo(github_repo: GitHubRepository) -> Repository:
    repo = Repository(
        name=github_repo.name,
        full_name=github_repo.full_name
    )

    return repo


class GitHubService(GitServiceProvider):
    api: Github
    user: AuthenticatedUser

    def __init__(self, token: str):
        self.api = Github(login_or_token=token)
        self.user = self.api.get_user()

    def get_repos(self) -> Iterable[Repository]:
        return map(convert_git_repo, self.user.get_repos())

    def create_repo(self, name: str, private: bool):
        ...

    def delete_repo(self, name: str):
        ...
