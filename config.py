import os
from distutils.util import strtobool
from os import getenv
from X.helpers.cmd import cmd
from dotenv import load_dotenv

load_dotenv("config.env")

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "⚡")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://graph.org/file/2bf3870c3b4df9960ccf8.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "𝐇ᴇʏ , 𝐇ᴏɴᴇʏ 𝐔sᴇʀ𝐁ᴏᴛ 𝐈s 𝐀ʟɪᴠᴇ 🥀")
API_HASH = getenv("API_HASH", "b93797389eab3cec8c697ae4f2418466)
API_ID = getenv("API_ID", "29044160")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "3.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "")
BOT_TOKEN = getenv("BOT_TOKEN", "none")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "SAIFALLBOT")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "DEAD_GRPCHAT")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://graph.org/file/2bf3870c3b4df9960ccf8.jpg")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://graph.org/file/687c31b4025478d6475d8.mp4")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6828253200").split()))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1002038548340, -1002131043993, -1002123837285]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
