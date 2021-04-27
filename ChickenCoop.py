import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#setting relay 1 and 2 as output pins
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)


relay1 = 16 
relay2 = 20
ON = 0
OFF = 1

def pin_trigger(pin,state):
    GPIO.output(pin, state)

instance = dht11.DHT11(pin=17)

while True:
    sensor_reading = instance.read()
    fahrenheit = ((sensor_reading.temperature * 9/5)+32)
    humidity = sensor_reading.humidity
    if sensor_reading.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temp: %d F" % (fahrenheit))
        print("Humidity: %d %%" % humidity)
    time.sleep(1)



