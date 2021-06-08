import paho.mqtt.client as mqtt
import json
import time
import serial

HOST = 'rainproject.online'

client = mqtt.Client()
client.connect(HOST, 1883, 60)
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
client.loop_start()
try:
    while True:
        ser.flush()
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').rstrip().split("space")
            time_now = time.strftime('%X')
            data = {
                "data":{
                    "temperature": message[0],
                    "humidity": message[1]
                },
                "device":"DHT11",
                "published_at": time_now
            }

            
            client.publish('/edge_device/data',json.dumps(data),1)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()