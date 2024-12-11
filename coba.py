import time
import RPi.GPIO as GPIO
#import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#DHT_SENSOR = 	Adafruit_DHT.DHT11
DHT_PIN = 4 
 
BUZZERS = [18,23,24]
 
for buzzer in BUZZERS :
   GPIO.setup(buzzer,GPIO.OUT)

def nyoba_tanpa_Adafruit():
   temperature = 15
   kelembaban = 30
   return temperature

while True:
    #_, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) 
    temperature = nyoba_tanpa_Adafruit()
    if temperature is not None:
        if temperature < 18:
            GPIO.output(BUZZERS[0], GPIO.HIGH)
            GPIO.output(BUZZERS[1], GPIO.LOW)
            GPIO.output(BUZZERS[2], GPIO.LOW)
        elif 18 <= temperature < 38:
            GPIO.output(BUZZERS[0], GPIO.LOW)
            GPIO.output(BUZZERS[1], GPIO.HIGH)
            GPIO.output(BUZZERS[2], GPIO.LOW)
        else:
            GPIO.output(BUZZERS[0], GPIO.LOW)
            GPIO.output(BUZZERS[1], GPIO.LOW)
            GPIO.output(BUZZERS[2], GPIO.HIGH)
    time.sleep(5)
