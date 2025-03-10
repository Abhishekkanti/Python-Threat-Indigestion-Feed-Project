import requests
import json
from threatintel_api.config import *
import AbuseIPDB
import sqlite
import URLhaus



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
