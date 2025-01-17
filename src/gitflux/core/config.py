from pathlib import Path
from typing import Dict

from pydantic_settings import BaseSettings, SettingsConfigDict

from .models import Profile

settings_file = Path.home() / '.config/gitflux/config.json'


class Settings(BaseSettings):
    profiles: Dict[str, Profile] = {}

    model_config = SettingsConfigDict(json_file=settings_file)

    def write(self):
        settings_file.write_text(self.model_dump_json(indent=4))


settings = Settings()
