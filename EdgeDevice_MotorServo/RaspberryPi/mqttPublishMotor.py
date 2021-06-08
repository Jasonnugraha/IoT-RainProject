import paho.mqtt.client as mqtt
import time
import json
import serial
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db

AUTH_PATH = "/home/pi/firebaseServiceAccount.json"
firebase_url = 'https://iot-final-project-mqtt-default-rtdb.asia-southeast1.firebasedatabase.app/'
cred = credentials.Certificate(AUTH_PATH)
firebase_admin.initialize_app(cred,{
    'databaseURL': firebase_url
})

HOST = 'rainproject.online'

device = '/dev/ttyACM0'
client = mqtt.Client()
client.connect(HOST, 1883, keepalive=60)

ref = db.reference('RainProject/sensor')
refControlValues = db.reference('ControlValues')

arduino = serial.Serial(port=device, baudrate= 9600, timeout= 1)
status = "OFF"
arduino.write(b'L')
clothesPrevious = True
rainPrevious = False
client.loop_start()
try:
    while True:

        time_now = time.strftime('%X')
        data = {
            "data":{
                "shadeStatus":status
            },
            "device":"SG90",
            "published_at": time_now
        }
        dataToSend = json.dumps(data)
        print(dataToSend)
        
        result = ref.get()
        controlValues = refControlValues.get()

        # working code
        #  if (result['rainingStatus']['value'] != rainPrevious ):
        if (controlValues['systemStatus'] == 'online'):
            if result['clothesHangingStatus']['value'] == False:
                arduino.write(b'L')
                # rainPrevious = False
                status = "OFF"
            if result['clothesHangingStatus']['value'] == True:
                if result['rainingStatus']['value'] == True:
                    if int(float(result['humidity']['value'])) > int(float(controlValues['humidityThreshold'])):
                        arduino.write(b'X')
                        status = "HIGH ALERT"
                    else:
                        arduino.write(b'H')
                        status = "ON"
                elif int(float(result['humidity']['value'])) > int(float(controlValues['humidityThreshold'])):
                    arduino.write(b'B')
                    status = "ALERT"
                    print("Humid")
                else:
                    arduino.write(b'L')
                    status = "OFF"
        else:
            arduino.write(b'L')
            status = "OFF"

        

        client.publish('/edge_device/data',dataToSend,1)
        time.sleep(1)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
