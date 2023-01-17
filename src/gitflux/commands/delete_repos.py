import click
from github import Github
from gitflux.utils import parse_repo_fullname


@click.command('delete-repos')
@click.argument('names', required=False, nargs=-1)
@click.option('--prefix', help='Prefix of repositories to delete.', type=str, default=None, required=False)
@click.pass_context
def delete_repos_command(ctx: click.Context, names: tuple[str], **options: dict):
    """Delete existing repositories."""

    github: Github = ctx.obj['github']

    user = github.get_user()

    if options['prefix'] is None:
        orgs = user.get_orgs()

        for name in names:
            owner, repo_name = parse_repo_fullname(name, user, orgs)
            owner.get_repo(repo_name).delete()
    else:
        if options['prefix'].lower() == 'all':
            if click.prompt(f'Delete ALL repositories of user: {user.login}, sure?', default='n').lower() == 'n':
                ctx.exit()

            repos = user.get_repos()
        else:
            if click.prompt(f'Delete ALL repositories with prefix: {options["prefix"]}, sure?', default='n').lower() == 'n':
                ctx.exit()

            repos = filter(lambda repo: repo.owner.login == options['prefix'], user.get_repos())

        for repo in repos:
            repo.delete()
