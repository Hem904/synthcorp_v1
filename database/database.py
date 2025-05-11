import psycopg2

def init_db():
    conn = psycopg2.connect(
        dbname="synthcorp",
        host="localhost",
        port="5432",
        user="postgres",
        password="admin"
    )
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS machines (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        type TEXT,
        current_state TEXT,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS production_logs (
        id SERIAL PRIMARY KEY,
        machine_name TEXT,
        action TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id SERIAL PRIMARY KEY,
        item_name TEXT UNIQUE NOT NULL,
        quantity INTEGER DEFAULT 0
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
        id SERIAL PRIMARY KEY,
        message TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
