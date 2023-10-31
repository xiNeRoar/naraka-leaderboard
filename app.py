from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # for flash messages

# Sample data
players = [
    {"rank": 1, "name": "Player A", "score": 5000},
    {"rank": 2, "name": "Player B", "score": 4800},
    {"rank": 3, "name": "Player C", "score": 4700},
    {"rank": 4, "name": "Player D", "score": 4600}
]

@app.route('/')
def index():
    return render_template('index.html', players=players)

@app.route('/update', methods=['POST'])
def update():
    # Get data from form
    name = request.form.get('name')
    score = request.form.get('score')
    # Update player data (for simplicity, we'll just append)
    players.append({"rank": len(players) + 1, "name": name, "score": int(score)})
    flash("Player updated successfully!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
