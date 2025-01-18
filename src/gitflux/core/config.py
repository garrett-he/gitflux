import json
from pathlib import Path
from typing import Dict

from pydantic_settings import BaseSettings

from .models import Profile

config_file = Path.home() / '.config/gitflux/config.json'


class Settings(BaseSettings):
    profiles: Dict[str, Profile] = {}

    @classmethod
    def load(cls):
        if not config_file.exists():
            return cls()

        data = json.load(config_file.open('r', encoding='utf-8'))

        return cls(**data)

    def save(self):
        data = self.model_dump()
        config_file.parent.mkdir(0o755, parents=True, exist_ok=True)

        config_file.write_text(json.dumps(data), encoding='utf-8')


settings = Settings.load()
