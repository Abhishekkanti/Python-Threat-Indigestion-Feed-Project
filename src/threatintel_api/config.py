# threatintel_api/config.py


#977c33f08808277f2955181690b4bbd52043d0b3197365e3b0156f7a29fdadda --Alien Vault otx
#176f6205aa52e7de790bde6598e89ff378a63564bfb6b7553de8aadb4cba57cb511112a9c922fc69--AbuseIPDB
#1801adb83c90d2c5627ed5768296517d0e0363ad57aa2c84da10104879733167--virustotal
#a6ed35fcee0f582647ea08ce3697d8086274e864ee79fc04--urlhaus


# API KEYS
ALIENVAULT_API_KEY = "977c33f08808277f2955181690b4bbd52043d0b3197365e3b0156f7a29fdadda"
ABUSEIPDB_API_KEY = "176f6205aa52e7de790bde6598e89ff378a63564bfb6b7553de8aadb4cba57cb511112a9c922fc69"
VIRUSTOTAL_API_KEY =  "93e8d4645cf80daadba443331006e207584a00a6c6e532caaa0929ee51ad681c" #"1801adb83c90d2c5627ed5768296517d0e0363ad57aa2c84da10104879733167"
URLHAUS_API_KEY = "a6ed35fcee0f582647ea08ce3697d8086274e864ee79fc04"


# API URLs
ALIENVAULT_URL =  "https://otx.alienvault.com/api/v1/pulses/subscribed"  #"https://otx.alienvault.com/api/v1/indicators/submitted_urls"  #"https://api.alintvault.com/v2/threats"
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/blacklist"
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/intelligence/search"
URLHAUS_URL = "https://urlhaus-api.abuse.ch/v1/urls/recent/limit/5"  #urls/recent/
PULSEDIVE_URL = "https://pulsedive.com"
PULSEDIVE_API_KEY = "d5918f9544e84c16988e5eb1badf6759f3727ad86a95f6a08b58ccdcbdf86a04"  # Get this from your Pulsedive account


#Snyk.io 
SYNK_URL = "https://security.snyk.io/vulns"
SYNK_API_KEY = "15a5aa03-9fe7-4834-9f3a-6b7df9e4049a"
