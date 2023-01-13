import click
from github import Github


@click.command('delete-repo')
@click.argument('name', required=True)
@click.pass_context
def delete_repo_command(ctx: click.Context, name: str):
    """Delete an existing repository."""

    github: Github = ctx.obj['github']
    github.get_user().get_repo(name).delete()
