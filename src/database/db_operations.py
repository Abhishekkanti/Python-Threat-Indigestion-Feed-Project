import sqlite3
from pathlib import Path

# Database path configuration
DB_PATH = "threat_intel.db"


def get_db_connection():
    """Create and return a database connection."""
    return sqlite3.connect(str(DB_PATH))

def init_database():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Create CVE details table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cve_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cve_id TEXT UNIQUE,
                title TEXT,
                date_published TEXT,
                severity TEXT,
                base_score REAL,
                description TEXT,
                affected_products TEXT,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create CVE references table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cve_references (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cve_id TEXT,
                url TEXT,
                tags TEXT,
                FOREIGN KEY (cve_id) REFERENCES cve_details (cve_id),
                UNIQUE(cve_id, url)
            )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"[-] Database initialization error: {e}")
        raise
    finally:
        conn.close()

def insert_cve_details(cve_id, title, date_published, severity, base_score, description, affected_products):
    """Insert or update CVE details in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT OR REPLACE INTO cve_details 
            (cve_id, title, date_published, severity, base_score, description, affected_products)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (cve_id, title, date_published, severity, base_score, description, affected_products))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"[-] Error inserting CVE details: {e}")
        return False
    finally:
        conn.close()

def insert_cve_reference(cve_id, url, tags):
    """Insert CVE reference into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT OR IGNORE INTO cve_references 
            (cve_id, url, tags)
            VALUES (?, ?, ?)
        """, (cve_id, url, tags))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"[-] Error inserting CVE reference: {e}")
        return False
    finally:
        conn.close()

# Initialize database when module is imported
init_database()