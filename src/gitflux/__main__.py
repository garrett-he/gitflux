import importlib
from typing import Annotated

import typer

from gitflux.cli.repo_commands import repo_app
from gitflux.core.config import settings
from gitflux.core.models import Profile, ProviderType

app = typer.Typer()
app.add_typer(repo_app, name='repo', help='Manage Git repositories.')


@app.callback()
def main(
    ctx: typer.Context,
    profile: Annotated[str, typer.Option(help='Profile to use', metavar='NAME')] = 'default'
):
    ctx.ensure_object(dict)

    if profile not in settings.profiles:
        typer.echo(f'Profile "{profile}" not found, try to generate:')

        settings.profiles[profile] = Profile(
            provider=typer.prompt('Provider', type=ProviderType, default='github'),
            access_token=typer.prompt('Access token', hide_input=True)
        )

        settings.save()

    provider_module = importlib.import_module(f'gitflux.providers.{settings.profiles[profile].provider}')
    ctx.obj['provider'] = provider_module.create_provider(settings.profiles[profile].access_token)


if __name__ == '__main__':
    app()
