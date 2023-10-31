from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('leaderboard.db') as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        );
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY,
            rule TEXT NOT NULL
        );
        """)

@app.route('/')
def index():
    with sqlite3.connect('leaderboard.db') as conn:
        players = conn.execute("SELECT * FROM players ORDER BY score DESC").fetchall()
        rules = conn.execute("SELECT * FROM rules").fetchall()
    return render_template('index.html', players=players, rules=rules)

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    with sqlite3.connect('leaderboard.db') as conn:
        if 'player' in data:
            conn.execute("INSERT INTO players (name, score) VALUES (?, ?)", (data['player']['name'], data['player']['score']))
        if 'rule' in data:
            conn.execute("INSERT INTO rules (rule) VALUES (?)", (data['rule'],))
    return jsonify(success=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
