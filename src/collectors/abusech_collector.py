import requests
import os
import json
from datetime import datetime

# Constants
RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/raw')
MALWAREBAZAAR_URL = "https://mb-api.abuse.ch/api/v1/"

def fetch_malwarebazaar_samples(limit=100):
    """
    Fetches recent malware sample hashes from Abuse.ch MalwareBazaar API.
    Returns list of hashes with metadata.
    """
    payload = {
        "query": "get_recent",
        "limit": limit
    }
    response = requests.post(MALWAREBAZAAR_URL, data=payload)
    if response.status_code == 200:
        data = response.json()
        if data.get("error", "") == "":
            return data.get("data", [])
        else:
            print(f"API error: {data.get('error')}")
            return []
    else:
        print(f"HTTP error: {response.status_code}")
        return []

def save_raw_data(data, filename=None):
    """
    Saves raw JSON data to data/raw directory with timestamped filename.
    """
    if not os.path.exists(RAW_DATA_DIR):
        os.makedirs(RAW_DATA_DIR)

    if filename is None:
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        filename = f"malwarebazaar_recent_{timestamp}.json"

    filepath = os.path.join(RAW_DATA_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Saved raw data to {filepath}")

def main():
    print("Fetching recent malware samples from MalwareBazaar...")
    samples = fetch_malwarebazaar_samples(limit=100)
    if samples:
        print(f"Fetched {len(samples)} samples.")
        save_raw_data(samples)
    else:
        print("No data fetched.")

if __name__ == "__main__":
    main()
