from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Function to get DB connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn


# Function to initialize database
def init_db():
    conn = get_db_connection()
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


# Route: Home
@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(users)


# Route: Add user
@app.route('/add/<name>')
def add_user(name):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES (%s);", (name,))
    conn.commit()

    cur.close()
    conn.close()

    return f"User '{name}' added successfully!"


# Run only when file is executed directly
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
