import click
from github import Github


@click.command('delete-repos')
@click.argument('names', required=True, nargs=-1)
@click.pass_context
def delete_repos_command(ctx: click.Context, names: tuple[str]):
    """Delete existing repositories."""

    github: Github = ctx.obj['github']

    for name in names:
        github.get_user().get_repo(name).delete()
