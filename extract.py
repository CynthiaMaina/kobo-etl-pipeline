import requests
import pandas as pd

from config import (
    KOBO_BASE_URL,
    KOBO_ASSET_ID,
    KOBO_API_TOKEN
)

def extract_data():
    #extract Kobo submissions and return them as a pandas dataframe

    url = f"{KOBO_BASE_URL}/api/v2/assets/{KOBO_ASSET_ID}/data/"
    headers = {
        "Authorization" : f"Token {KOBO_API_TOKEN}"
    }
    try:
        all_results = []
        while url:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            data = response.json()
            all_results.extend(data.get('results',[]))
            url = data.get('next')
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error connecting to Kobo API: {e}")

    print(f"Extracted: {len(all_results)} records")
    

    df = pd.json_normalize(all_results)

    return df