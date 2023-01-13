from .list_repos import list_repos_command
from .create_repo import create_repo_command
from .delete_repo import delete_repo_command

command_group = [list_repos_command, create_repo_command, delete_repo_command]
