import requests
import csv
import sqlite3
from sqlite import DB_FILE, create_db

data = {
    'meta': {
        'generatedAt': '2025-02-26T13:09:07+00:00'
    },
    'data': [
        {
            'ipAddress': '193.68.89.52',
            'countryCode': 'NL', 
            'abuseConfidenceScore': 100,
            'lastReportedAt': '2025-02-26T12:17:01+00:00'
        },
        {
            'ipAddress': '185.226.197.12',
            'countryCode': 'NL',
            'abuseConfidenceScore': 100,
            'lastReportedAt': '2025-02-26T12:17:01+00:00'
        },
        {
            'ipAddress': '92.191.96.7',
            'countryCode': 'ES',
            'abuseConfidenceScore': 100,
            'lastReportedAt': '2025-02-26T12:17:01+00:00'
        }
    ]
}


# for ip in data['data']:
#     print(ip['ipAddress'] + " " + str(ip['abuseConfidenceScore']))

# url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"

# response = requests.get(url)

# print(response.text)
# create_db()
# try:
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO malicious_urls (url_id, url, source, threat) VALUES (10001, 'bb.com', 'urlhaus', 'malware')")
#     conn.commit()
# except sqlite3.Error as e:
#     print(f"[-] SQLite Error: {e}")
# finally:
#     conn.close()