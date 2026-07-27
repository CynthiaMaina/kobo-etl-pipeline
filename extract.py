import requests
import pandas as pd

from config import (
    KOBO_BASE_URL,
    KOBO_ASSET_ID,
    KOBO_API_TOKEN
)

def extract_data():
    #extract training data and return it as a pandas dataframe

    url = f"{KOBO_BASE_URL}/api/v2/assets/{KOBO_ASSET_ID}/data/"
    headers = {
        "Authorization" : f"Token {KOBO_API_TOKEN}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error connecting to Kobo API: {e}")

    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        raise Exception(f"Request failed : {response.text}")
    
    data = response.json()
    df = pd.json_normalize(data["results"])

    return df