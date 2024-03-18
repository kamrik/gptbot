import os
from os import getenv
import dotenv

file_dir = os.path.dirname(os.path.abspath(__file__))

dotenv.load_dotenv(dotenv_path= os.path.join(file_dir, "azure.env"))
# envirionments (or define here)
LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG").upper()
BOT_TOKEN = getenv("BOT_TOKEN")
ORG_ID = getenv("ORG_ID")
API_KEY = getenv("API_KEY")
AZURE_ENDPOINT = getenv("AZURE_ENDPOINT")
API_PROVIDER = getenv("API_PROVIDER", "openai")
