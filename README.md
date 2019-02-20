# 2IO70-COM
## Communication protocol specifications for the 2IO70 project of 2019
## V1.0

This protocol uses MQTT to send and receive signals between bots.

### About MQTT:
MQTT is a lightweight M2M (Machine to Machine) or IoT protocol.
It's main points of focus are data integrity and reliability

### Why MQTT:
MQTT is perfect for the communication between our robots, because it is implemented in many languages.
This means that all the robots can use the language they prefer, and are not limited by our protocol.

More info about MQTT can be found on mqtt.org


## Specifications:
MQTT uses channels. Each one of these channels is used to either transmit or receive signals to one bot
This means that in total we will have 6 channels, 2 channels per bot and 3 bots in total.

Each bot has a number. This number corresponds to your group number. This means that bot 1 is the conveyor belt.

The channels use a specific naming convention.
NAME CHANNEL = 'Bot[group number]_[T/R]'

T means that the specific bot uses this channel to transmit data to the master
R means that the specific bot uses this channel to receive data from the master

A group should only use it's specified channels, and not communicate with the other channels

## Signals

Certain signals can be received over MQTT. The signals and their meaning are:
```
available	--	A bot should send this signal to the system within 0.5 second once said bot has finished it's task and is ready for a new one

takeItem	--	A bot receives this signal when they should take exactly one item from the belt. This signal is send only when the bot has indicated it is available

emergency	--	A bot should send this signal when a problem occurs. If a bot recieves this signal it should stop it's functions.

placeItem	--	A bot should send this signal when they place an item on the belt
```

A few python examples of the code are placed in the public repository on github.
Note. These examples are written in python 2.7, but MQTT is also available for newer versions of python 3
 




