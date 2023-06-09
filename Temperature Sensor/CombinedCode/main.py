import time
import machine

from umqttsimple import MQTTClient
import ubinascii
import json

# My custom ledFunctions to interact with all the LEDs on my board.
import ledFunctions as leds

# Phillip's code to display two digit numbers on the matrix display
import doubleDigits as display

# My library for the motorized slider.
from motorSlider import MotorSlider

# For handling the BME280 sensor.
import BME280

# To create an MQTT client, we need to get the ESP unique ID
client_id = ubinascii.hexlify(machine.unique_id())

# MQTT Broker Data for PWP project
# Home Assistant with mosquitto addon (remember to open port 1883 in the router)
mqtt_server = 'philipphomeassistant.duckdns.org'
mqtt_port = 1883
mqtt_user = 'mqtt-user'
mqtt_pw = 'PhilippSmartHomeMQTT'

# The current State gets stored here and updated with the Slider AND the MQTT topic
currentState = 0

# MQTT Topics
DATA_TOPIC = b'pwpTemperatureSensor'
STATE_TOPIC = b'pwpTemperatureSensorState'

#############
# Functions #
#############

# Returns the current readings from the BME280 sensor (optionally without units due to them being assigned in Home Assistant).
# You should wrap this in try except.
def getSensorReadings(units):
    # BME280 readings according to https://randomnerdtutorials.com/micropython-bme280-esp32-esp8266/
    global bme
    temperature = bme.temperature
    humidity = bme.humidity
    pressure = bme.pressure

    print(f'Current sensor readings are: temperature: {temperature}, humidity: {humidity}, pressure: {pressure}')

    # Optionally remove units before returning (as they may be assigned in Home Assistant already for example)
    if(not units):
        temperature = temperature.replace('C','')
        humidity = humidity.replace('%','')
        pressure = pressure.replace('hPa','')

    return (temperature, humidity, pressure)
        
# Connects to the MQTT broker specified within the mqtt_server variable.
def connectBroker():
    global client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pw
    client = MQTTClient(client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pw)
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to MQTT broker: ' + mqtt_server)
    return client

# Resets the ESP on failed connection in order to try again later.
def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
    
# Publishes SensorData to the TemperatureSensor Topic in JSON format
def publishData(temp, hum, pres):
    client.publish(DATA_TOPIC, json.dumps({"temperature": str(temp), "humidity": str(hum), "pressure": str(pres)}))

        
# Publishes a message to all topics listed in topics2pub.
def publishState(state):
    client.publish(STATE_TOPIC, str.encode(state))
    
# Connects to a topic on the connected MQTT broker. 
def subscribeTopic(topic):
    client.subscribe(topic)
    print('Subscribed to topic: ' + str(topic))

# This callback function is called, when a message is received and should then begin handling that message.
def sub_cb(topic, msg):
    print('Inc. message: [%s] %s' % (topic, msg))
    # Handle incoming state here
    if topic == STATE_TOPIC:
        try:
            global currentState
            currentState = msg
        except:
            print('Couldn\'t handle temperature \'%s\'. Ignoring it instead.' % msg)

# Tries reading available messages and reboots on crash.
def tryRead():
    try:
        # Check whether a pending message from the server is available. If yes they are delivered to the callback function specified above.
        client.check_msg()

    except OSError as e:
        restart_and_reconnect() # On crash just reboot


#####################
# Execute on start: #
#####################

# BME280 sensor: assignment of I2C parameters
i2c = machine.I2C(scl=machine.Pin(19), sda=machine.Pin(18), freq=10000)
# Initialize BME sensor
bme = BME280.BME280(i2c=i2c)

#Initialization of motorSlider
ms = MotorSlider(34,32,16,17)

try:
    client = connectBroker() # Connect to broker
    print('MQTT connection successful!')
    
    # Subscribe to the State Topic
    subscribeTopic(b'TemperatureSensorStateHA')

except OSError as e:
    print('Failed MQTT connection with error: %s' % e)
    restart_and_reconnect() # Try again later on fail.

###################
# Execution loop: #
###################
while True:
    # Try fetching and publishing current sensor readings.
    try:
        # Publish sensor data here with temperature, humidity, pressure
        (temp, hum, pres) = getSensorReadings(units=False)
        publishData(temp, hum, pres)
    except Exception as e:
        print(f'Could not get and publish sensor readings due to error: {e}')
    
    # Publish State here
    publishState(str(1))
    
    # Check for new Messages here
    tryRead()
    
    #percentValue = round(ms.readPCT() * 100)
    #display.displayNumbers(percentValue)
    time.sleep_ms(500)