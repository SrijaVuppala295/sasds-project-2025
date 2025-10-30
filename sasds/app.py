"""Flask application entry point"""
# Flask application entry point
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "SASDS Project"

if __name__ == '__main__':
    app.run(debug=True)
