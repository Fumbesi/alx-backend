#!/usr/bin/env python3
"""
Basic Flask app with a single route.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route for the home page.

    :return: Rendered template with title and header.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
