from flask import Flask, render_template, url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    with app.test_request_context():
        return redirect(url_for('static', filename='index.html'))
    

@app.route('/hello')
def hello():
    return 'Hello, World'


with app.test_request_context():
    print(url_for('static', filename='index.html'))