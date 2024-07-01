from .list_repos import list_repos_command
from .create_repos import create_repos_command
from .delete_repo import delete_repo_command

command_group = [list_repos_command, create_repos_command, delete_repo_command]
