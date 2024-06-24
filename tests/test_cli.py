import json
import tempfile
import importlib.metadata
from pathlib import Path

from chance import chance
from pytest_mock import MockerFixture
from click.testing import CliRunner
from gitflux.__main__ import cli


def test_cli_version(cli_runner: CliRunner):
    result = cli_runner.invoke(cli, ['--version'])

    if result.exception:
        print(result.output)

    assert not result.exception
    assert result.output.strip() == importlib.metadata.version('gitflux')


def test_cli_init_config(cli_runner: CliRunner, mocker: MockerFixture):
    token = chance.hex_hash(40)
    mocker.patch('click.prompt', return_value=token)

    config_file = Path(tempfile.mktemp())
    result = cli_runner.invoke(cli, ['--init-config', '--config-file', config_file])

    assert not result.exception
    assert config_file.is_file()
    assert json.load(config_file.open('r', encoding='utf-8')) == {'accessToken': token}

    config_file.unlink()
