import http.client
import json
import requests

from threatintel_api.config import *


def get_Alienvault_pulses():
    """Fetching the latest threats from AlienVault OTX API."""
    try:
        header = {
            "X-OTX-API-KEY": ALIENVAULT_API_KEY}
        para = {
            "limit": 10,
            'q': 'malware'}

        result = requests.get(ALIENVAULT_URL, params= para,  headers=header)
        result.raise_for_status()  # Raise error for HTTP issues

        #converting reveived data in json
        data = result.json()

        return data  # Returns the threat intelligence data

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching data from AlienVault: {e}")
        #return None


print(get_Alienvault_pulses())
