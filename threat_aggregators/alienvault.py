import requests
from threatintel_api.config import ALIENVAULT_API_KEY, ALIENVAULT_URL

def get_alienvault_pulses():
    """Fetching the latest threats from AlienVault OTX API."""
    try:
        header = {"X-OTX-API-KEY": ALIENVAULT_API_KEY}
        para = {"limit": 10, 'q': 'malware'}

        result = requests.get(ALIENVAULT_URL, params=para, headers=header)
        result.raise_for_status()
        return result.json()

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching data from AlienVault: {e}")
        return None
    

#print(get_Alienvault_pulses())