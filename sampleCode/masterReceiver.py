import paho.mqtt.client as mqtt
#The callback for when the clients receives a CONNACK response from the server
MQTT_SERVER = "192.168.0.2"
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
	
	#subscribing in on_connect() means that if we lose the connnection and 
	# reconnec then subscriptions will be renewed
    client.subscribe("bot1/to_master")
    client.subscribe("bot2/to_master")
    client.subscribe("bot3/to_master")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)


client.loop_forever()
