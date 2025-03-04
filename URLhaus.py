import requests
from threatintel_api.config import *


def get_urlhaus_malicious_urls():
    try:
        result = requests.get(URLHAUS_URL, timeout=10)
        result.raise_for_status()  # Raise an error for HTTP issues

        data = result.json()

        if data.get("query_status") == "ok":
            return data # Returns the list of malicious URLs

        print("[-] Error: No data retrieved from URLhaus.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching data from URLhaus: {e}")
        return None


#res = get_urlhaus_malicious_urls()
# print(res)
# if res:
#     for entry in res[:5]:  # Print first 5 entries
#         print(f"[+] {entry['url']} - Threat: {entry['threat']} - Status: {entry['status']}")