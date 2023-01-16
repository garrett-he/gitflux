import click
from github import Github
from gitflux.utils import parse_repo_fullname


@click.command('create-repos')
@click.argument('names', required=True, nargs=-1)
@click.option('--private', help='Private repository.', is_flag=True, default=True)
@click.pass_context
def create_repos_command(ctx: click.Context, names: tuple[str], **options: dict):
    """Create new repositories."""

    github: Github = ctx.obj['github']

    user = github.get_user()
    orgs = user.get_orgs()

    for name in names:
        owner, repo_name = parse_repo_fullname(name, user, orgs)
        owner.create_repo(repo_name, private=options['private'])
