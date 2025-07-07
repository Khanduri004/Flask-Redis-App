from flask import Flask, render_template
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = r.incr('hits')
    return render_template('index.html', message=f"Hello! You have visited this page {count} times.")

