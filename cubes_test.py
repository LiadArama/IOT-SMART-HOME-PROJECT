import paho.mqtt.client as mqtt
import time
import random

# broker IP adress:
broker = "broker.hivemq.com"
running_time = 90 #in sec
topic = 'matzi/all'
port = 80 #for using web sockets

def on_log(client, userdata, level, buf):
        print("log: "+buf)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code= ", rc)
def on_disconnect(client, userdata, flags, rc=0):
        print("DisConnected result code "+str(rc))
def on_message(client, userdata, msg):
        topic = msg.topic
        m_decode = str(msg.payload.decode("utf-8", "ignore"))
        print("message received: ", m_decode)

r=random.randrange(1,10000) # for creating unique client ID
clientname="IOT_test-"+str(r)
client = mqtt.Client(clientname, clean_session=True) # create new client instance

client.on_connect = on_connect  #bind call back function
client.on_disconnect = on_disconnect
#client.on_log=on_log
client.on_message = on_message
client.username_pw_set(username="MATZI",password="MATZI")


print("Connecting to broker ", broker)
client.connect(broker, port) #connect to broker

# Following is an example for code turning a Relay device 'On':
#device_ID = "3PI_16167641"
#client.publish("matzi/0/"+device_ID, ' {"type":"set_state", "action":"set_value", "addr":0, "cname":"ONOFF", "value":1}')
# and consequently 'OFF':
#client.publish("matzi/0/"+device_ID, ' {"type":"set_state", "action":"set_value", "addr":0, "cname":"ONOFF", "value":0}')

# Next loop will publishing all messages during running time
client.loop_start()
client.publish("matzi/test", "test1")
#client.subscribe("matzi/0/3PI_16145805/sts")
client.subscribe("matzi/#")
time.sleep(running_time)
client.loop_stop()
client.disconnect() # disconnect
print("End of script run")
