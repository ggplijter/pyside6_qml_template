from os import makedirs
from pathlib import Path

FILEDIR = Path(__file__).parent
ROOT_DIR = (FILEDIR / "../../.").resolve()
VENV_DIR = ROOT_DIR / ".venv/Scripts"
APP_DIR = ROOT_DIR / "app"

PYTHON_EXE = VENV_DIR / "python.exe"
RCC_EXE = VENV_DIR / "pyside6-rcc.exe"


LOG_DIR = APP_DIR / "log"
makedirs(LOG_DIR, exist_ok=True)
LOGGING_CONFIG = FILEDIR / "./logging_config.json"

RESOURCES_DIR = APP_DIR / "resources"
makedirs(RESOURCES_DIR, exist_ok=True)

FILEPATH_ERROR_DUMP = LOG_DIR / "{date_str}_error_dump.png"



