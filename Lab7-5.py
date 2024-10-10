import RPi.GPIO as GPIO
import drivers
from time import sleep
 
 
BUTTON1 = 27
BUTTON2 = 17
 
 
display = drivers.Lcd()
display.lcd_clear()
 
btState = 0
 
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
GPIO.add_event_detect(BUTTON1, GPIO.FALLING)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING)
 
try:
    while True:
   
        if GPIO.event_detected(BUTTON1):
            print("Button 1 Pressed ")
            btState += 1
            if btState == 1:
                display.lcd_clear()
                display.lcd_display_string("Ikclass", 1)
                display.lcd_display_string("116630462012-1", 2)
 
            if btState == 2:
                display.lcd_clear()
                display.lcd_display_string("sasiwimon", 1)
                display.lcd_display_string("116630462004-8", 2)
                btState = 0
 
       
        if GPIO.event_detected(BUTTON2):
            print("Button 2 Pressed - Exiting")
            display.lcd_clear()  
            display.lcd_display_string("Bye...", 1)  
            sleep(2)  
            break  
       
 
except KeyboardInterrupt:
 
    display.lcd_clear()
    print("\nBye...")
finally:
    GPIO.cleanup()
