# 2IO70-COM
## Communication protocol specifications for the 2IO70 project of 2019
## V1.1
![map of belt](https://raw.githubusercontent.com/JelleTUE/2IO70-COM/master/images/plattegrond.png)  
This protocol uses MQTT to send and receive signals between bots.

### About MQTT
MQTT is a lightweight M2M (Machine to Machine) or IoT protocol.
It's main points of focus are data integrity and reliability

### Why MQTT
MQTT is perfect for the communication between our robots, because it is implemented in many languages.
This means that all the robots can use the language they prefer, and are not limited by our protocol.

More info about MQTT can be found on mqtt.org


## Specifications

### Channels
MQTT uses channels. Each one of these channels is used to either transmit or receive signals to one bot
This means that in total we will have 6 channels, 2 channels per bot and 3 bots in total.

Each bot has a number. This number corresponds to your group number. This means that bot 1 is the conveyor belt.

The channels use a specific naming convention.
NAME CHANNEL = 'Bot[group number]_[T/R]'

T means that the specific bot uses this channel to transmit data to the master
R means that the specific bot uses this channel to receive data from the master

A group should only use it's specified channels, and not communicate with the other channels!

![image of system](https://raw.githubusercontent.com/JelleTUE/2IO70-COM/master/images/brokerSystem.png)

### Signals

Certain signals can be sent and received over your MQTT channel.
Signals you may send:  
```
emergency		--	A bot sends this signal when it detects an error, and wants the entire system to go into emergency mode.

available		--	'[Group 3 / 4]' A bot sends this signal to the system once said bot has finished it's task and is ready for a new one.

placeItem		--	A bot sends this signal when they want to place an item on the belt. This bot will either receive a placeItemGranted or a placeItemDenied signal.

finishedInstruction	--	'[Group 2]' A bot sends this signal when it is finished with their predefined sequence.
```

Signals you might receive:  
```
takeItem		--	A bot receives this signal when they should take exactly one disk from the belt. The disk will arrive in approximately 2 seconds. This signal is send only when the bot has indicated it is available

emergency		--	A bot receives this signal when a problem has been detected by the system. If a bot receives this signal it should stop it's functions.

placeItemGranted	-- 	'[Group 3 / 4]' A bot receives this signal when their request to place an item has been granted. The bot should place the item on the belt within 3 seconds

placeItemDenied		-- 	'[Group 3 / 4]' A bot receives this signal when their request to place an item has been denied. Situations like this could occur during a sequence where the conveyor belt needs to be clean

startSequence		--	'[Group 2'] The system sends this signal at most once per 2 minutes, when it is ready to provide a predefined sequence.

```

Note that initially all bots will be considered free. There is no need to send an available signal at the boot of the system!

Some example communication:
![sequence communication](https://raw.githubusercontent.com/JelleTUE/2IO70-COM/master/images/sequence.png)  
![sequence communication](https://raw.githubusercontent.com/JelleTUE/2IO70-COM/master/images/placement.png)

A few python examples of the code are placed in the public repository on github.
 




