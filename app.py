import os
import shutil
import time
import threading
from flask import Flask, send_from_directory, render_template_string

# Init Flask
app = Flask(__name__)
DEBUG = False

@app.route('/')
def index():
    return 'ASTC Encoder Service Running'

if __name__ == '__main__':
    app.run(debug=DEBUG, use_reloader=False, host='0.0.0.0', port=3000)
