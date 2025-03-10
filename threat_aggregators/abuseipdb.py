import requests
from threatintel_api.config import ABUSEIPDB_API_KEY, ABUSEIPDB_URL

def get_abuseipdb_pulse():
    """Fetch malicious IPs from AbuseIPDB."""
    try:
        header = {
            "Key": ABUSEIPDB_API_KEY,
            "Accept": "application/json"
        }
        para = {
            "confidenceMinimum": 50,
            "limit": 10
        }

        result = requests.get(ABUSEIPDB_URL, headers=header, params=para, timeout=10)
        result.raise_for_status()
        return result.json()

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching data from AbuseIPDB: {e}")
        return None