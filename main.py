from typing import Final
import os
from dotenv import load_dotenv


# 0 - LOAD TOKEN FROM .ENV FILE
load_dotenv()  # loads the token from .env file
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
# print(TOKEN) # -> works
