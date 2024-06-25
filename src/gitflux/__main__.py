import json
from pathlib import Path

import click
from github import Github
from gitflux.commands import command_group


def init_config(ctx: click.Context, _, value: bool):
    if not value or ctx.resilient_parsing:
        return

    config_file = Path(ctx.params['config_file'])
    if config_file.is_file() and click.prompt(f'Configuration file "{config_file}" already exists, overwrite?', type=str, default='n').lower() in ['n', 'no', '0']:
        ctx.exit()

    with config_file.open('w', encoding='utf-8') as fp:
        json.dump({
            'accessToken': click.prompt('Access token', type=str, hide_input=True)
        }, fp, indent=4, ensure_ascii=False)

    config_file.chmod(0o600)
    ctx.exit()


@click.group(commands=command_group)
@click.version_option(message='%(version)s')
@click.option('--config-file', help='Path of configuration file.', type=click.Path(dir_okay=False), expose_value=True, is_eager=True, default=Path(Path.home(), '.gitfluxrc'))
@click.option('--init-config', help='Initialize configurations.', is_flag=True, callback=init_config, expose_value=False)
@click.pass_context
def cli(ctx: click.Context, config_file: Path):
    """A nested command-line utility that helps you manage repositories hosted on GitHub."""

    ctx.ensure_object(dict)

    config_file = Path(config_file)

    if not config_file.is_file():
        raise FileNotFoundError(f'Configuration file "{config_file}" not found, try with --init-config.')

    config = json.loads(config_file.read_text(encoding='utf-8'))
    ctx.obj['github'] = Github(login_or_token=config['accessToken'])


if __name__ == '__main__':
    cli()
