import sqlite3


def create_table():
    conn = sqlite3.connect('whois.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS whois_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_name TEXT NOT NULL,
            status TEXT,
            registrant_id TEXT,
            registrant_name TEXT,
            organization TEXT,
            address TEXT,
            city TEXT,
            region TEXT,
            country TEXT,
            phone TEXT,
            email TEXT,
            registrar TEXT,
            nameservers TEXT,
            expiration_date TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_to_db(whois_data):
    conn = sqlite3.connect('whois.db')
    cursor = conn.cursor()
    columns = (
        "domain_name", "status", "registrant_id", "registrant_name",
        "organization", "address", "city", "region", "country",
        "phone", "email", "registrar", "nameservers", "expiration_date"
    )

    values = [
        whois_data['domain_name'], ','.join(whois_data['status']),
        whois_data['registrant_id'], whois_data['registrant_name'],
        whois_data['organization'], whois_data['address'],
        whois_data['city'], whois_data['region'], whois_data['country'],
        whois_data['phone'], whois_data['email'], whois_data['registrar'],
        ','.join(whois_data['nameservers']), whois_data['expiration_date']
    ]

    cursor.execute(
        f'''
        INSERT INTO whois_data ({", ".join(columns)})
        VALUES ({", ".join(["?"] * len(columns))})
        ''',
        values
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()