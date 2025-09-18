# config/configuration.py (o como se llame)
from pathlib import Path
import sys
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

def _env_path() -> Path:
    # Cuando corre como ejecutable (--onefile), el .env debe ir JUNTO al binario
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent / ".env"
    # En desarrollo, ajusta a donde tengas el .env (root del repo, etc.)
    # Si tu .env está en el root del proyecto, y este archivo vive en config/,
    # subir un nivel suele ser lo correcto:
    return Path(__file__).resolve().parent.parent / ".env"

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=None,               # NO uses ruta relativa
        env_file_encoding='utf-8',
        env_prefix='',               # sin prefijo
        case_sensitive=False         # permite TE_TOKEN/te_token
    )

    te_base_url: str = "https://api.thousandeyes.com/v7/"
    te_token: str = Field(..., alias="TE_TOKEN")   # <<-- alias explícito

    org_id: int = 138579
    aid: int = 150378
    window_size: int = 30

    @property
    def te_headers(self) -> dict:
        return {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.te_token}'}

    @property
    def te_headers_hal(self) -> dict:
        return {'Accept': 'application/hal+json', 'Authorization': f'Bearer {self.te_token}'}

# Cargar el .env desde una ruta ABSOLUTA
load_dotenv(_env_path(), override=False)

# Instanciar config
config = Config()
