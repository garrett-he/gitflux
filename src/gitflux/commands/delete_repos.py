import click
from github import Github
from gitflux.utils import parse_repo_fullname


@click.command('delete-repos')
@click.argument('names', required=True, nargs=-1)
@click.pass_context
def delete_repos_command(ctx: click.Context, names: tuple[str]):
    """Delete existing repositories."""

    github: Github = ctx.obj['github']

    user = github.get_user()
    orgs = user.get_orgs()

    for name in names:
        owner, repo_name = parse_repo_fullname(name, user, orgs)
        owner.get_repo(repo_name).delete()
