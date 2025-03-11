import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

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


def sort_and_insert_data(data):
    # Create dictionaries to store items by type
    sorted_url = {}
    sorted_domain = {}
    sorted_hash = {}
    sorted_ipv4 = {}
    sorted_cve = {}

    # First sort the data by type
    for item in data:
        item_type = item['type']
        if item_type == 'URL':
            sorted_url[item['id']] = item
        elif item_type == 'domain':
            sorted_domain[item['id']] = item
        elif item_type == 'FileHash-MD5':
            sorted_hash[item['id']] = item
        elif item_type == 'IPv4':
            sorted_ipv4[item['id']] = item
        elif item_type == 'CVE':
            sorted_cve[item['id']] = item

    # Insert URLs into malicious_urls table
    for url_id, item in sorted_url.items():
        insert_url(
            url_id=url_id,
            url=item['indicator'],
            source="AlienVault",
            threat=item.get('description', 'Unknown')
        )

    # Insert hashes into malicious_hashes table
    for _, item in sorted_hash.items():
        insert_hash(
            file_hash=item['indicator'],
            source="AlienVault",
            description=item.get('description', '')
        )

    # Insert IPs into malicious_ips table
    for _, item in sorted_ipv4.items():
        insert_ip(
            ip=item['indicator'],
            source="AlienVault",
            confidence=item.get('confidence', 100)  # Default confidence of 100
        )
        
    # Insert CVEs into CVE table
    for _, item in sorted_cve.items():
        insert_cve(
            indicator=item['indicator'],
            description=item.get('description', ''),
            severity=item.get('severity', 'Unknown')
        )

  #  print("Data has been sorted and inserted into the database successfully.")


#sort_and_insert_data(indicator_data)

