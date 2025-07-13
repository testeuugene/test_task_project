from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

DB_PARAMS = {
    'dbname': 'weatherdb',
    'user': 'postgres',
    'password': 'postgres',
    'host': os.environ.get("DB_HOST", "db"),
    'port': 5432,
}

def get_connection():
    return psycopg2.connect(**DB_PARAMS)

@app.route("/ping")
def ping():
    return "<h1>PONG</h1>"

@app.route("/health")
def health():
    return jsonify({"status": "HEALTHY"})

@app.route("/list")
def list_weather():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT city, temperature FROM weather;")
        rows = cur.fetchall()
    html = "<h1>Weather List</h1><ul>"
    for city, temp in rows:
        html += f"<li>{city}: {temp}°C</li>"
    html += "</ul>"
    return html

@app.route("/add", methods=["POST"])
def add():
    city = request.form.get("city")
    temperature = request.form.get("temperature")
    if not city or not temperature:
        return "Missing data", 400
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO weather (city, temperature) VALUES (%s, %s);", (city, int(temperature)))
        conn.commit()
    return f"Added {city} with {temperature}°C", 201

if __name__ == "__main__":
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS weather (city TEXT, temperature INT);")
        cur.execute("SELECT COUNT(*) FROM weather;")
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute("INSERT INTO weather (city, temperature) VALUES ('London', 20), ('Moscow', 25);")
        conn.commit()
    app.run(host="0.0.0.0", port=8080)
