import requests
from threatintel_api.config import VIRUSTOTAL_API_KEY, VIRUSTOTAL_URL

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
    """Fetch VirusTotal reputation for a URL."""
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