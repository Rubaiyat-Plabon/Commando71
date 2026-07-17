from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    if os.path.exists('logs.txt'):
        with open('logs.txt', 'r') as f:
            data = f.read().strip()
        return jsonify({'data': data})
    return jsonify({'data': 'Waiting for data...'})

if __name__ == '__main__':
    app.run(port=5000)