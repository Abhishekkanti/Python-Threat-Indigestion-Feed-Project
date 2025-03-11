indicator_data  =[
{'id': 4036382742, 'indicator': 'https://fondfbr.ru/de/artikel/german-child-abuse-de/', 'type': 'URL', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4036382743, 'indicator': 'https://fondfbr.ru/de/artikel/germany-ampel-against-opposition-de/', 'type': 'URL', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4036382744, 'indicator': 'https://fondfbr.ru/de/artikel/germany-censorship-de/', 'type': 'URL', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},

{'id': 4036382745, 'indicator': 'aktuell-nachricht.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4036382746, 'indicator': 'aktuellde.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4036382747, 'indicator': 'aktuellenews-berlin.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},

{'id': 4033347346, 'indicator': 'd8e826a6cb2ce2c9ee74242e993a7874', 'type': 'FileHash-MD5', 'created': '2025-02-05T16:10:17', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4033347347, 'indicator': 'ebaba93172f6bcb47b1bb4a270542e98', 'type': 'FileHash-MD5', 'created': '2025-02-05T16:10:17', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4033347348, 'indicator': 'ed691e1e20160346094c08d2cebf0f32', 'type': 'FileHash-MD5', 'created': '2025-02-05T16:10:17', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None}, 

{'id': 4030020893, 'indicator': '5.10.250.240', 'type': 'IPv4', 'created': '2025-03-06T23:02:42', 'content': '', 'title': '', 'description': '', 'expiration': '2025-04-05T23:00:00', 'is_active': 1, 'role': None},
#{'id': 4043716687, 'indicator': '79.132.128.77', 'type': 'IPv4', 'created': '2025-03-06T23:02:42', 'content': '', 'title': '', 'description': '', 'expiration': '2025-04-05T23:00:00', 'is_active': 1, 'role': None},
#{'id': 4043716688, 'indicator': '89.187.28.253', 'type': 'IPv4', 'created': '2025-03-06T23:02:42', 'content': '', 'title': '', 'description': '', 'expiration': '2025-04-05T23:00:00', 'is_active': 1, 'role': None},
#{'id': 3618081367, 'indicator': '91.202.233.18', 'type': 'IPv4', 'created': '2025-03-06T23:02:42', 'content': '', 'title': '', 'description': '', 'expiration': '2025-04-05T23:00:00', 'is_active': 1, 'role': None}, 

{'id': 4036392140, 'indicator': 'CVE-2025-0994', 'type': 'CVE', 'created': '2025-02-20T02:49:25', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
#{'id': 4036392141, 'indicator': 'CVE-2025-0995', 'type': 'CVE', 'created': '2025-02-20T02:49:25', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
]


# data = (
#     data[0]['id'],
#     data['indicator'],
#     data.get('source', ''),  # Using get() with default value in case source is not in input
#     data.get('description', ''),
#     data['created']
# )

#for data in indicator_data :
 #   print(data['id'], data['type'], data['indicator'],  data.get('source', ''), data.get('description', ''), data['created'])
 


from sqlite import insert_url, insert_hash, insert_ip, insert_cve

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

    print("Data has been sorted and inserted into the database successfully.")


sort_and_insert_data(indicator_data)

