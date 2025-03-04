import sqlite3

DB_FILE = "threat_intel.db"

connect = sqlite3.connect(DB_FILE)
cursor = connect.cursor()

def create_db():
    """Create SQLite database and tables if they don't exist."""
    connect = sqlite3.connect(DB_FILE)
    cursor = connect.cursor()

    # Create tables for IPs, URLs, and Hashes
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS CVE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            indicator TEXT,
            description TEXT,
            severity TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS malicious_ips(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            source TEXT,
            threat TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS malicious_hashes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_hash TEXT UNIQUE,
            source TEXT,
            description TEXT 
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )


    # Create fresh table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS malicious_urls(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url_id INTEGER UNIQUE,
            url TEXT,
            source TEXT,
            threat TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    connect.commit()
    connect.close()

#GPT

def insert_cve(indicator, description, severity):
    """Insert a CVEs into the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO CVEs (indicator, description, severity) VALUES (?, ?, ?)", (indicator, description, severity))
        conn.commit()
    except sqlite3.Error as e:
        print(f"[-] SQLite Error: {e}")
    finally:
        conn.close()


def insert_ip(ip, source, confidence):
    """Insert a malicious IP into the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO malicious_ips (ip, source, confidence) VALUES (?, ?, ?)", (ip, source, confidence))
        conn.commit()
    except sqlite3.Error as e:
        print(f"[-] SQLite Error: {e}")
    finally:
        conn.close()


def insert_url(url_id, url, source, threat):
    """Insert a malicious URL into the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO malicious_urls 
            (url_id, url, source, threat) 
            VALUES (?, ?, ?, ?)
        """, (url_id, url, source, threat))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"[-] SQLite Error: {e}")
    finally:
        conn.close()


def insert_hash(file_hash, source, description):
    """Insert a malicious file hash into the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO malicious_hashes (file_hash, source, description) VALUES (?, ?, ?)", (file_hash, source, description))
        conn.commit()
    except sqlite3.Error as e:
        print(f"[-] SQLite Error: {e}")
    finally:
        conn.close()

def fetch_all(table):
    """Fetch all records from a given table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    results = cursor.fetchall()
    conn.close()
    return results

# # Initialize database
create_db()
#
#     # Example data insertions
# insert_ip("192.168.1.100", "AbuseIPDB")
#insert_url("00001", "fb.com", "urlhaus", "malware download")
# insert_hash("44d88612fea8a8f36de82e1278abb02f", "VirusTotal", "WannaCry Ransomware")
# insert_cve("CVE 2025-24200", "Vulnerability in iphone devices.", "High")
#
#     # Fetch & print stored data
# print("Malicious IPs:", fetch_all("malicious_ips"))
# print("Malicious URLs:", fetch_all("malicious_urls"))
# print("Malicious Hashes:", fetch_all("malicious_hashes"))
# print("CVE: ", fetch_all("CVEs"))
#

# conn= sqlite3.connect(DB_FILE)
# cursor = conn.cursor()
# cursor.execute("ALTER TABLE CVEs ADD COLUMN indicator TEXT ")