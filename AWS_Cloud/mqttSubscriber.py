import paho.mqtt.client as mqtt
import json
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

MQTT_HOST='127.0.0.1'
MQTT_PORT=1883
SERVICE_ACCOUNT_PATH='/var/iot/firebaseServiceAccount.json'
FIREBASE_URL='https://iot-final-project-mqtt-default-rtdb.asia-southeast1.firebasedatabase.app/'

cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)

firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_URL
})

dbReference = db.reference('RainProject/sensor')

# the callback funciton for when the client receives a CONNACK response from server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("/edge_device/data")

def on_message(client, userdata, msg):
    print(msg.topic + " " +str(msg.payload))
    payload = json.loads(msg.payload)
    updateData = {}

    if payload['device'] == 'FC37':
        updateData = {
            "rainingStatus": {
                "value": payload['data']['rainingStatus'],
                "published_at": payload['published_at']
            }
        }
    elif payload['device'] == 'DHT11':
        updateData = {
            "temperature":{
                "value": payload['data']['temperature'],
                "published_at": payload['published_at']
            },
            "humidity":{
                "value": payload['data']['humidity'],
                "published_at": payload['published_at']
            }
        }
    elif payload['device'] == 'HC-SR04':
        updateData = {
            "clothesHangingStatus":{
                "value": payload['data']['clothesHangingStatus'],
                "published_at": payload['published_at']
            }
        }
    elif payload['device']  == 'SG90':
        updateData = {
            "shadeStatus":{
                "value": payload['data']['shadeStatus'],
                "published_at": payload['published_at']
            }
        }
    
    if updateData != {}:
        dbReference.update(updateData)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60)

client.loop_forever()