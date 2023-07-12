'''Utility for accessing environment configuration.'''

import os

from typing import Final
from dotenv import load_dotenv

load_dotenv(os.path.relpath("data.env"))

DISCORD_BOT_TOKEN: Final[str] = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_TEST_GUILD: Final[str] = os.getenv("DISCORD_TEST_GUILD")

SUBSONIC_SERVER: Final[str] = os.getenv("SUBSONIC_SERVER")
SUBSONIC_USER: Final[str] = os.getenv("SUBSONIC_USER")
SUBSONIC_PASSWORD: Final[str] = os.getenv("SUBSONIC_PASSWORD")
