# Virus Total Refinement

import requests
from threatintel_api.config import *

#VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3"

def get_vt_ip_reputation(ip):
    """Fetch VirusTotal reputation for an IP address."""
    url = f"{VIRUSTOTAL_URL}/ip_addresses/{ip}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching IP reputation: {e}")
        return None


def get_vt_url_reputation(url_id):
    """Fetch VirusTotal reputation for a URL (requires SHA256-encoded URL ID)."""
    url = f"{VIRUSTOTAL_URL}/urls/{url_id}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching URL reputation: {e}")
        return None


def submit_vt_url(scan_url):
    """Submit a new URL to VirusTotal for scanning."""
    url = f"{VIRUSTOTAL_URL}/urls"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    data = {"url": scan_url}

    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"[-] Error submitting URL to VirusTotal: {e}")
        return None

def get_vt_file_reputation(file_hash):
    """Fetch VirusTotal reputation for a file hash (MD5, SHA-1, SHA-256)."""
    url = f"{VIRUSTOTAL_URL}/files/{file_hash}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching file reputation: {e}")
        return None


# Example usage
#
# ip_result = get_vt_ip_reputation("8.8.8.8")
# if ip_result:
#     print(f"IP Reputation: {ip_result}")
#
# print("\n")
# print("\n")
# print("\n")
# print("\n")
# print("\n")
#
# file_result = get_vt_file_reputation("44d88612fea8a8f36de82e1278abb02f")
# if file_result:
#    print(f"File Reputation: {file_result}")
