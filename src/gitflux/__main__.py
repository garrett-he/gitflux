import click


@click.command()
@click.version_option(message='%(version)s')
def cli():
    """A nested command-line utility that helps you manage repositories hosted on GitHub."""


if __name__ == '__main__':
    cli()
