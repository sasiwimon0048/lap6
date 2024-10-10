from flask import Flask, render_template_string, redirect, url_for
import RPi.GPIO as GPIO
import atexit
 
GPIO.setmode(GPIO.BCM)
 
LED_PINS = {
    'green': 17,
    'red': 27
}
 
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
 
led_status = {
    'green': 'OFF',
    'red': 'OFF'
}
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template_string('''
        <html>
        <head>
            <title>LED Controller</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f0f0f0;
                    padding: 50px;
                }
                h1 {
                    color: #333;
                }
                .led-status {
                    margin: 20px;
                    font-size: 24px;
                    font-weight: bold;
                }
                .button-container {
                    margin: 10px;
                }
                a {
                    padding: 15px 25px;
                    font-size: 16px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    margin: 5px;
                    text-decoration: none;
                    color: white;
                }
                .on {
                    background-color: #4CAF50; /* à¸ªà¸µà¹à¸à¸µà¸¢à¸§ */
                }
                .off {
                    background-color: #f44336; /* à¸ªà¸µà¹à¸à¸ */
                }
            </style>
        </head>
        <body>
            <h1>LED Controller</h1>
            <div class="led-status">LED 1 (Green) - {{ led_status['green'] }}</div>
            <div class="button-container">
                <a href="/led1/on" class="on">LED 1 ON</a>
                <a href="/led1/off" class="off">LED 1 OFF</a>
            </div>
            <div class="led-status">LED 2 (Red) - {{ led_status['red'] }}</div>
            <div class="button-container">
                <a href="/led2/on" class="on">LED 2 ON</a>
                <a href="/led2/off" class="off">LED 2 OFF</a>
            </div>
        </body>
        </html>
    ''', led_status=led_status)
 
@app.route('/led1/on')
def led1_on():
    led_status['green'] = 'ON'
    GPIO.output(LED_PINS['green'], GPIO.HIGH)
    return redirect(url_for('index'))
 
@app.route('/led1/off')
def led1_off():
    led_status['green'] = 'OFF'
    GPIO.output(LED_PINS['green'], GPIO.LOW)
    return redirect(url_for('index'))
 
@app.route('/led2/on')
def led2_on():
    led_status['red'] = 'ON'
    GPIO.output(LED_PINS['red'], GPIO.HIGH)
    return redirect(url_for('index'))
 
@app.route('/led2/off')
def led2_off():
    led_status['red'] = 'OFF'
    GPIO.output(LED_PINS['red'], GPIO.LOW)
    return redirect(url_for('index'))
 
atexit.register(GPIO.cleanup)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
