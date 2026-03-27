from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        return conn
    except Exception as e:
        print("DB connection failed:", e)
        return None


def init_db():
    conn = get_db_connection()
    if conn is None:
        print("Skipping DB init (DB not available)")
        return

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.route('/')
def home():
    conn = get_db_connection()
    if conn is None:
        return "Database not available"

    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(users)


@app.route('/add/<name>')
def add_user(name):
    conn = get_db_connection()
    if conn is None:
        return "Database not available"

    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s);", (name,))
    conn.commit()

    cur.close()
    conn.close()

    return f"User '{name}' added successfully!"


if __name__ == '__main__':
    # IMPORTANT: this is safe now
    init_db()
    app.run(host='0.0.0.0', port=5000)
