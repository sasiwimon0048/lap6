from flask import Flask, render_template_string
 
app = Flask(__name__)
 
# สถานะของ LED
led1_status = "OFF"
led2_status = "OFF"
 
@app.route('/')
def index():
    return render_template_string('''
<h1>LED Control</h1>
<p>LED 1 - {{ led1 }}</p>
<p>LED 2 - {{ led2 }}</p>
    ''', led1=led1_status, led2=led2_status)
 
@app.route('/led1/on')
def led1_on():
    global led1_status
    led1_status = "ON"
    return index()
 
@app.route('/led1/off')
def led1_off():
    global led1_status
    led1_status = "OFF"
    return index()
 
@app.route('/led2/on')
def led2_on():
    global led2_status
    led2_status = "ON"
    return index()
 
@app.route('/led2/off')
def led2_off():
    global led2_status
    led2_status = "OFF"
    return index()
 
if __name__ == '__main__':
