import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sys, os, time


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send(time, value):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Host port keepalive bin_addr
    # client.connect("172.24.20.26", 1883, 60)
    client.connect("192.168.1.72", 1883, 60)

    # To test if work, on server use command :
    # mosquitto_sub -d -t paho/temperature
    client.publish("paho/temperature", value)
    print("Msg sent")


# Check Arguments
if len(sys.argv) != 2:
    print("Need an argument")
    print("python " + sys.argv[0] + " [file_name]")
    sys.exit(2)

# Check If EXIST and not EMPTY
file = sys.argv[1]
if not os.path.isfile(file):
    print("File not existing")
    sys.exit(2)
if os.stat(file).st_size == 0:
    print("File empty")
    sys.exit(2)

# Read file line by line and split
# split line TIME1 _ VALUE1
#            TIME2 _ VALUE2
#             ...  _  ...
#
# For each value (line) send to pytt
f = open(file,"r")
for line in f:
    split = line.split()
    send(split[0], split[1])
    print(split)
    time.sleep(5)
