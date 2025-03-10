indicator_data  =[
{'id': 4036382742, 'indicator': 'https://fondfbr.ru/de/artikel/german-child-abuse-de/', 'type': 'URL', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382743, 'indicator': 'https://fondfbr.ru/de/artikel/germany-ampel-against-opposition-de/', 'type': 'URL', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382744, 'indicator': 'https://fondfbr.ru/de/artikel/germany-censorship-de/', 'type': 'URL', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382745, 'indicator': 'aktuell-nachricht.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382746, 'indicator': 'aktuellde.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382747, 'indicator': 'aktuellenews-berlin.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382748, 'indicator': 'aktuelles-aus-nurnberg.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382749, 'indicator': 'alles-klar-hamburg.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None},
{'id': 4036382750, 'indicator': 'alles-wichtig-news.de', 'type': 'domain', 'created': '2025-02-13T10:39:45', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1, 'role': None}
]




# data = (
#     data[0]['id'],
#     data['indicator'],
#     data.get('source', ''),  # Using get() with default value in case source is not in input
#     data.get('description', ''),
#     data['created']
# )

for data in indicator_data :
    print("_"* 10)
    print(data['id'], data['type'], data['indicator'],  data.get('source', ''), data.get('description', ''), data['created'])
    print("_"* 10)

