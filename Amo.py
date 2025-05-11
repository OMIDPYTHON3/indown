import logging
from flask import Flask
from threading import Thread

app = Flask(__name__)

# خاموش کردن لاگ‌ها
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)  # غیرفعال‌سازی لاگ Werkzeug

@app.route('/')
def index():
    return "Alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()