import click
from github import Github


@click.command('create-repos')
@click.argument('names', required=True, nargs=-1)
@click.option('--private', help='Private repository.', is_flag=True, default=True)
@click.pass_context
def create_repos_command(ctx: click.Context, names: tuple[str], **options: dict):
    """Create new repositories."""

    github: Github = ctx.obj['github']

    user = github.get_user()

    for name in names:
        user.create_repo(name, private=options['private'])
