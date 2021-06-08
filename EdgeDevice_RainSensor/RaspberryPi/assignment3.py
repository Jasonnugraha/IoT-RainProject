import serial
import paho.mqtt.client as mqtt
import os
import time
import json
import sys
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db


#DEFINE HOST IN THE CLOUD
data_interval = 0.01
device = '/dev/ttyS0'
AWS_HOST = 'rainproject.online'

AUTH_PATH = "firebaseServiceAccount.json"
firebase_url = 'https://iot-final-project-mqtt-default-rtdb.asia-southeast1.firebasedatabase.app/'
cred = credentials.Certificate(AUTH_PATH)
firebase_admin.initialize_app(cred,{
    'databaseURL': firebase_url
})

refControlValues = db.reference('ControlValues')


#set up the arduino port
device = '/dev/ttyACM0'
#start the serial communication with baud 9600
arduino = serial.Serial(device, 9600, timeout=1)

# PREPARING THE CONNECTION TO THE SERVER
client = mqtt.Client()
client.connect(AWS_HOST, 1883, 60)
client.loop_start()

try:
    #loop infinitely
    while True:
        arduino.flush()
        #check whether the arduino sent something
        if arduino.in_waiting > 0:
            #read what the arduino sent, while decoding the message
            data = arduino.readline().decode('utf-8').rstrip()
            #print the data for checking
            print(data)
            
            #get the values from the database
            result = refControlValues.get()
            #if the rain sensor value detects water
            if int(data) <= int(result['rainThreshold']):
                rainingStatus = True
            else:
                rainingStatus = False

            time_now = time.strftime('%X')
            data = {
                "data":{
                    'rainingStatus':rainingStatus
                },
                "device":"FC37",
                "published_at": time_now
            }
            
            #SEND VALUE TO THE AWS USING MQTT
            client.publish('/edge_device/data',json.dumps(data),1)

                
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()