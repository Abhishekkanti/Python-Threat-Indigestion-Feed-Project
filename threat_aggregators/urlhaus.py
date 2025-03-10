import requests
from threatintel_api.config import URLHAUS_URL

def get_urlhaus_malicious_urls():
    """Fetch recent malicious URLs from URLhaus."""
    try:
        result = requests.get(URLHAUS_URL, timeout=10)
        result.raise_for_status()

        data = result.json()
        if data.get("query_status") == "ok":
            return data

        print("[-] Error: No data retrieved from URLhaus.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching data from URLhaus: {e}")
        return None