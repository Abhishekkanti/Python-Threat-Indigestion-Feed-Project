import requests
import json
from threatintel_api.config import *


def get_Abuseipdb_pulse():
    try:
        header = {
            "Key": ABUSEIPDB_API_KEY,
            "Accept": "application/json"}
        para = {
            "confidenceMinimum": 50,
            "limit": 10}

        result = requests.get(ABUSEIPDB_URL, headers=header, params=para, timeout=10)
        result.raise_for_status()  # Raise error for HTTP issues

        data = result.json()
        return data

        if data.get("query_status") == "ok":
            return data["data"]  # Returns the list of malicious URLs

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching data from AbuseIPDB: {e}")
        return None


#print(get_Abuseipdb_pulse())
