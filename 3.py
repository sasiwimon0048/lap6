import RPi.GPIO as GPIO
import time
 
# Set up the GPIO pin numbers
BUTTON_PIN = 10
LED_PIN = 8
 
# Set up the GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)
 
# Initialize the LED state
led_on = False
 
try:
    while True:
        # Check if the button is pressed
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            # Toggle the LED state
            led_on = not led_on
            GPIO.output(LED_PIN, led_on)
           
            # Display the LED state
            if led_on:
                print("LED => ON")
            else:
                print("LED => OFF")
           
            # Wait for button release
            while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                time.sleep(0.1)
       
        # Short delay to prevent button bounce
        time.sleep(0.1)
       
except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
