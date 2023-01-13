import click
from github import Github


@click.command('create-repo')
@click.argument('name', required=True)
@click.option('--private', help='Private repository.', is_flag=True, default=True)
@click.pass_context
def create_repo_command(ctx: click.Context, name: str, **options: dict):
    """Create a new repository."""

    github: Github = ctx.obj['github']
    github.get_user().create_repo(name, private=options['private'])
