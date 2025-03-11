import requests
import json
from src.threatintel_api.config import *
from src.threat_aggregators.abuseipdb import get_abuseipdb_pulse
from src.threat_aggregators.urlhaus import get_urlhaus_malicious_urls
from src.threat_aggregators.virustotal import fetch_cve_details, store_cve_details



# #AbuseIPDB Pulse 
# try:
#     #Reciving data from AbuseIPDB
#     data = AbuseIPDB.get_Abuseipdb_pulse()
#     #Creating a list of ips & confidence to store in the database
#     ips = []
#     confidence = []
#     for ip in data['data']:
#         ips.append(ip['ipAddress'])
#         confidence.append(ip['abuseConfidenceScore'])

#     #Inserting ips into the database
#     for i in range(len(ips)):
#         sqlite.insert_ip(ips[i], "AbuseIPDB", confidence[i])
#     print("[-] AbuseIPDB data inserted successfully")
# except Exception as e:
#     print("[-] Error: ", e)


#URLhaus
# try:
#     temp = URLhaus.get_urlhaus_malicious_urls()
#     data = temp['urls']
   
#     for urls in data:
#         url_id = urls['id']
#         url = urls['url']
#         threat = urls['threat']
        
#         if url_id and url:  # Only insert if we have the required fields
#             sqlite.insert_url(url_id, url, "URLhaus", threat)
#         else:
#             print(f"Missing required fields in URL data: {urls}")
    
#     print("[-] URLhaus data inserted successfully")
# except Exception as e:
#         print("[-] Error: ", e)


# src/
# ├── config/
# │   ├── __init__.py
# │   └── api_config.py
# ├── database/
# │   ├── __init__.py
# │   └── db_operations.py
# ├── data/
# │   └── threat_intel.db
# └── threat_aggregators/
#     ├── __init__.py
#     └── virustotal.py

if __name__ == "__main__":
    # Test the functionality
    test_cve_id = "CVE-2017-9841"
    print(f"[+] Fetching details for {test_cve_id}")
    cve_details = fetch_cve_details(test_cve_id)
    if cve_details:
        success = store_cve_details(cve_details)
        if success:
            print(f"[+] Successfully stored details for {test_cve_id}")
        else:
            print(f"[-] Failed to store details for {test_cve_id}")

