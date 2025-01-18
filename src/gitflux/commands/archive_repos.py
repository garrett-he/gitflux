import click

from gitflux.providers import GitServiceProvider


@click.command('archive-repos')
@click.argument('names', required=False, nargs=-1)
@click.pass_context
def archive_repos_command(ctx: click.Context, names: tuple[str], **options: dict):
    """
    Archive existing repositories.
    """

    provider: GitServiceProvider = ctx.obj['provider']

    for name in names:
        provider.archive_repo(name)
