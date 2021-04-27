#this can only be run on the Rpi
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import SendEmail

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

relay1 = 20
relay2 = 16 

#setting relay 1 and 2 as output pins
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)

#relay is backwards and this turns the pins off
ON = 0
OFF = 1
GPIO.output(relay1,OFF)
GPIO.output(relay2,OFF)

def pin_trigger(pin,state):
    GPIO.output(pin, state)

def tempTrigger(temp):
    tooHot = 76
    tooCold = 64
    idealTemp = range(65,75,1)
    extremeHot = 95
    extremeCold = 50
    if temp >= tooHot:
        pin_trigger(relay1,ON)
        #if temp >= extremeHot:
            #SendEmail()
    if temp <= tooCold:
        pin_trigger(relay2,ON)
        #if temp <= extremeCold:
            #SendEmail()
    elif temp == idealTemp:
        pin_trigger(relay1,OFF)
        pin_trigger(relay2,OFF)


instance = dht11.DHT11(pin=17)

while True:
    sensor_reading = instance.read()
    fahrenheit = ((sensor_reading.temperature * 9/5)+32)
    humidity = sensor_reading.humidity
    if sensor_reading.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temp: %d F" % (fahrenheit))
        print("Humidity: %d %%" % humidity)
        tempTrigger(fahrenheit)
        
    time.sleep(1)



