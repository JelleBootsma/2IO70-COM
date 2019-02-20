import paho.mqtt.publish as publish

while(True):
    message = raw_input("Wat wil je verzenden? ")
    publish.single("bot1/to_master", message, hostname = "192.168.1.34")

    print("done")
