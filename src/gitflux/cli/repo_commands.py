import typer

repo_app = typer.Typer()


@repo_app.command(name='list')
def list_repos(ctx: typer.Context):
    """
    List all remote repositories.
    """
    provider: GitServiceProvider = ctx.obj.get('provider')

    for repo in provider.get_repos():
        typer.echo(repo.full_name)


import click

from gitflux.providers import GitServiceProvider


@repo_app.command(name='create')
def create_repos(ctx: click.Context, names: tuple[str], private: bool = True):
    """
    Create new repositories.
    """

    provider: GitServiceProvider = ctx.obj.get('provider')

    for name in names:
        provider.create_repo(name, private=private)


@repo_app.command(name='delete')
def delete_repos(ctx: click.Context, names: tuple[str], prefix: str | None = None):
    """
    Delete existing repositories.
    """

    provider: GitServiceProvider = ctx.obj.get('provider')

    for name in names:
        provider.delete_repo(name)

    if prefix is None or click.prompt(f'Delete ALL repositories prefixed: {prefix}?', default='n').lower() == 'n':
        ctx.exit()

    for name in map(lambda repo: repo.full_name, filter(lambda repo: repo.get_prefix() == prefix, provider.get_repos())):
        provider.delete_repo(name)

@repo_app.command(name='archive')
def archive_repos_command(ctx: click.Context, names: tuple[str]):
    """
    Archive existing repositories.
    """

    provider: GitServiceProvider = ctx.obj.get('provider')

    for name in names:
        provider.archive_repo(name)
