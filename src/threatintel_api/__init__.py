"""Threat Intelligence API Package
This package provides access to various threat intelligence APIs and their configurations.
"""
from .config import (    # AlienVault OTX
    ALIENVAULT_API_KEY,    ALIENVAULT_URL,
        # AbuseIPDB
    ABUSEIPDB_API_KEY,    ABUSEIPDB_URL,
        # VirusTotal
    VIRUSTOTAL_API_KEY,    VIRUSTOTAL_URL,
        # URLhaus
    URLHAUS_API_KEY,    URLHAUS_URL,
        # Snyk
    SYNK_API_KEY,    SYNK_URL
)

__all__ = [    'ALIENVAULT_API_KEY',
    'ALIENVAULT_URL',    'ABUSEIPDB_API_KEY',
    'ABUSEIPDB_URL',    'VIRUSTOTAL_API_KEY',
    'VIRUSTOTAL_URL',    'URLHAUS_API_KEY',
    'URLHAUS_URL',    'SYNK_API_KEY',
    'SYNK_URL'
]




















"""
Threat Intelligence API Package

This package provides access to various threat intelligence APIs and their configurations.
"""

from .config import (
    # AlienVault OTX
    ALIENVAULT_API_KEY,
    ALIENVAULT_URL,
    
    # AbuseIPDB
    ABUSEIPDB_API_KEY,
    ABUSEIPDB_URL,
    
    # VirusTotal
    VIRUSTOTAL_API_KEY,
    VIRUSTOTAL_URL,
    
    # URLhaus
    URLHAUS_API_KEY,
    URLHAUS_URL,
    
    # Snyk
    SYNK_API_KEY,
    SYNK_URL
)

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = [
    'ALIENVAULT_API_KEY',
    'ALIENVAULT_URL',
    'ABUSEIPDB_API_KEY',
    'ABUSEIPDB_URL',
    'VIRUSTOTAL_API_KEY',
    'VIRUSTOTAL_URL',
    'URLHAUS_API_KEY',
    'URLHAUS_URL',
    'SYNK_API_KEY',
    'SYNK_URL'
]
