import importlib.metadata
from click.testing import CliRunner
from gitflux.__main__ import main


def test_cli_version(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ['--version'])

    if result.exception:
        print(result.output)

    assert not result.exception
    assert result.output.strip() == importlib.metadata.version('gitflux')
