import os
from dotenv import load_dotenv

#lets load variables from.env file
load_dotenv()
KOBO_BASE_URL = os.getenv("KOBO_BASE_URL")
KOBO_ASSET_ID = os.getenv("KOBO_ASSET_ID")
KOBO_API_TOKEN = os.getenv("KOBO_API_TOKEN")