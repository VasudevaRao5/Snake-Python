# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'cloud run'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
