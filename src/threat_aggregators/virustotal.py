
import os
import sys
from pathlib import Path

# Get the absolute path of the project root directory
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
sys.path.append(str(project_root))

import requests
import json
from src.threatintel_api.config import VIRUSTOTAL_API_KEY, VIRUSTOTAL_URL
from src.database.db_operations import insert_cve_details, insert_cve_reference


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


# CIRCL CVE Search API endpoint for CVE details

# Function to fetch CVE details
def fetch_cve_details(cve_id):
    """Fetch CVE details from CIRCL CVE Search API."""
    CIRCL_API_URL = "https://cve.circl.lu/api/cve/"
    url = f"{CIRCL_API_URL}{cve_id}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching CVE details: {e}")
        return None


def store_cve_details(cve_data):
    """Store CVE details in the database."""
    try:
        # Extract basic information from new API structure
        cve_id = cve_data.get('cveMetadata', {}).get('cveId')
        if not cve_id:
            print("[-] Error: CVE ID not found in data")
            return False

        # Get container data
        cna_container = cve_data.get('containers', {}).get('cna', {})
        
        # Extract CVSS data safely
        metrics = cna_container.get('metrics', [{}])[0]
        cvss_data = metrics.get('cvssV3_1', {})
        cvss = cvss_data.get('baseScore', 0.0)
        severity = cvss_data.get('baseSeverity', get_severity_from_cvss(cvss))
        
        # Get description
        descriptions = cna_container.get('descriptions', [])
        description = next((desc['value'] for desc in descriptions if desc.get('lang') == 'en-US'), '')
        
        # Get affected products
        affected_products = set()
        for affected in cna_container.get('affected', []):
            vendor = affected.get('vendor', '')
            product = affected.get('product', '')
            if vendor and product:
                affected_products.add(f"{vendor}:{product}")
            # Add CPEs if available
            affected_products.update(affected.get('cpes', []))
        
        # Convert set to JSON string for storage
        affected_products_json = json.dumps(list(affected_products))
        
        # Store main CVE details
        success = insert_cve_details(
            cve_id=cve_id,
            title=cna_container.get('title', '')[:100],
            date_published=cve_data.get('cveMetadata', {}).get('datePublished', ''),
            severity=severity,
            base_score=cvss,
            description=description,
            affected_products=affected_products_json
        )
        
        if not success:
            return False

        # Store references
        references = cna_container.get('references', [])
        for ref in references:
            if ref.get('url'):  # Ensure reference URL exists
                insert_cve_reference(cve_id, ref['url'], ','.join(ref.get('tags', [])))
                
        return True
        
    except Exception as e:
        print(f"[-] Error storing CVE details: {e}")
        return False

def get_severity_from_cvss(cvss_score):
    """Convert CVSS score to severity rating."""
    try:
        score = float(cvss_score)
        if score == 0.0:
            return "NONE"
        elif score < 4.0:
            return "LOW"
        elif score < 7.0:
            return "MEDIUM"
        elif score < 9.0:
            return "HIGH"
        else:
            return "CRITICAL"
    except (ValueError, TypeError):
        return "UNKNOWN"




