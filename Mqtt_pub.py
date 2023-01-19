import paho.mqtt.client as mqtt
import time

broker = "172.31.80.40"
port = 1883

client = mqtt.Client()

while True:
    try:
     client.connect(broker,port)
     print('Broker connected')
     client.publish('sacet/a11','hii')
     time.sleep(4)

    except:
     print('Broker Connection Failure')
