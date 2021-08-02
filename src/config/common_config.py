import os
from pathlib import Path

from logs.logger import log

# Prefix that the bot uses to discover envars settings for the bots
ENVAR_PREFIX = "BOT_"

CONFIG_ROOT = os.path.dirname(os.path.abspath(__file__))
config_root = Path(CONFIG_ROOT)
REPO_ROOT = config_root.parents[1].absolute()
SRC_ROOT = os.path.join(REPO_ROOT, "src")
ENV_FILE = os.path.join(REPO_ROOT, ".env")

log.info(f"config root: {CONFIG_ROOT}")
log.info(f"repo root: {REPO_ROOT}")
log.info(f"src root: {SRC_ROOT}")
