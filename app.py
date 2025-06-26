from flask import Flask, render_template
import json

app = Flask(__name__)

with open('cameras.json') as f:
    cameras = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', cameras=cameras)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
