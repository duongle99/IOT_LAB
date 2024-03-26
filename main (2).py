import sys
from Adafruit_IO import MQTTClient
import time
import random
from uart import *


AIO_FEED_IDs = ["BBC_LED", "BBC_FAN"]
AIO_USERNAME = "dlhcmut"
AIO_KEY = "aio_WVaY13WXXMdhR2r1EDfTQN82ZM9X"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)
    if feed_id == "BBC_LED":
        if payload == "a":
            writeData(1)
        else:
            writeData(2)
    if feed_id == "BBC_FAN":
        if payload == "c":
            writeData(3)
        else:
            writeData(4)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


while True:
    readSerial(client)
    time.sleep(1)