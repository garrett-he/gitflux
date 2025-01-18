import json
from pathlib import Path
from typing import Dict

from pydantic_settings import BaseSettings, JsonConfigSettingsSource, PydanticBaseSettingsSource

from .models import Profile

config_file = Path.home() / '.config/gitflux/config.json'


class Settings(BaseSettings):
    profiles: Dict[str, Profile] = {}

    def save(self):
        data = self.model_dump()
        config_file.parent.mkdir(0o755, parents=True, exist_ok=True)

        config_file.write_text(json.dumps(data, indent=4), encoding='utf-8')

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (JsonConfigSettingsSource(settings_cls, json_file=str(config_file)),)


settings = Settings()
