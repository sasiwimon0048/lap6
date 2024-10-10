from flask import Flask

app = Flask(__name__)

@app.route('/add/<a>/<b>')
def add(a, b):
    ans = float(a) + float(b)
    return f'<h3>{a} + {b} = {ans}</h3>'

@app.route('/sub/<a>/<b>')
def subtract(a, b):
    ans = float(a) - float(b)
    return f'<h3>{a} - {b} = {ans}</h3>'

@app.route('/mul/<a>/<b>')
def multiply(a, b):
    ans = float(a) * float(b)
    return f'<h3>{a} * {b} = {ans}</h3>'

@app.route('/div/<a>/<b>')
def divide(a, b):
    if float(b) != 0:
        ans = float(a) / float(b)
        return f'<h3>{a} / {b} = {ans}</h3>'
    else:
        return '<h3>Error: Division by zero is not allowed.</h3>'

@app.route('/')
def index():
    return 'Lab 9_4'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
