import os
from distutils.util import strtobool as sb

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
DB_URL = os.getenv("DATABASE_URL")
HEROKU_API = os.getenv("HEROKU_API")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
PY_SESSION = os.getenv("PYROGRAM_SESSION")
PREFIX = os.environ.get("PREFIX", ".")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
PM_AUTO_BAN = os.getenv('PM_AUTO_BAN', 'False')
