import paho.mqtt.client as mqtt
import os
import time
import json
import sys
import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase authentication and initialization
AUTH_PATH = "/home/pi/firebaseServiceAccount.json"
firebase_url = 'https://iot-final-project-mqtt-default-rtdb.asia-southeast1.firebasedatabase.app/'
cred = credentials.Certificate(AUTH_PATH)
firebase_admin.initialize_app(cred,{
    'databaseURL': firebase_url
})
refControlValues = db.reference('ControlValues')

#DEFINE DATA SUCH AS THINGSBOARD HOST IN THE CLOUD AND ACCESS TOKEN
data_interval = 0.01
device = '/dev/ttyS2'
HOST = 'rainproject.online'


#ARDUINO SERIAL READING
arduino = serial.Serial(port = device, baudrate = 9600, timeout = 1)
INTERVAL = 1
next_reading = time.time()

# PREPARING THE CONNECTION TO THE SERVER
client = mqtt.Client()
client.connect(HOST, 1883, 60)
client.loop_start()

try:
    while True:
        arduino.flush()
        #CHECKS WHETHER THE ARDUINO HAS PENDING DATA OR NOT
        if arduino.in_waiting > 0:
            #GETTING VALUE FROM SERIAL
            distance = arduino.readline().decode('utf-8').rstrip()
            distanceValue = distance
            
            # Printing data (distance) to check the value
            print("Distance of the object: " + distance)
            
            # Fetching data from the firebase for the threshold
            request = refControlValues.get()
            print("Threshold: " + request["sonicThreshold"])
            
            #Check the data, if distance detected is true and according to the threshold
            if int(distance) < int(request["sonicThreshold"]):
                ClothesStatus = True
                arduino.write(b'H') #Send data via serial to the arduino to read for turning on the led light
            else:
                ClothesStatus = False
                arduino.write(b'L') #Send data via serial to the arduino to read for turning off the led light
            
            time_now = time.strftime('%X')
            data = {
                "data":{
                   'clothesHangingStatus':ClothesStatus 
                },
                "device":"HC-SR04",
                "published_at": time_now
            }
            
            #Used to publish into Firebase using MQTT
            client.publish('/edge_device/data',json.dumps(data),1)
            next_reading += INTERVAL
            sleep_time = next_reading - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()