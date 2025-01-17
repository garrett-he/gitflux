import importlib

import click

from gitflux.commands import command_group
from gitflux.core.config import settings
from gitflux.core.models import Profile


@click.group(commands=command_group)
@click.version_option(message='%(version)s')
@click.option('-p', '--profile-name', help='Name of profile to use.', type=str, required=False, default='default')
@click.pass_context
def main(ctx: click.Context, profile_name: str):
    """
    A command-line utility that helps you manage repositories hosted on Git service providers.
    """

    ctx.ensure_object(dict)

    if profile_name not in settings.profiles:
        click.echo(f'Profile "{profile_name}" not found, try to generate:')

        settings.profiles[profile_name] = Profile(
            provider=click.prompt('Provider', type=click.Choice(['github', 'gitee']), default='github'),
            access_token=click.prompt('Access token', hide_input=True)
        )

        settings.write()

    profile = settings.profiles[profile_name]
    provider_module = importlib.import_module(f'gitflux.providers.{profile.provider}')

    ctx.obj['provider'] = provider_module.create_provider(profile.access_token)


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
