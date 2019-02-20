import paho.mqtt.publish as publish

while(True):
    message = raw_input("Wat wil je verzenden? ")
    publish.single("bot1/to_slave", message, hostname = "localhost")

    print("done")
