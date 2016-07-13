# Pytt
MQTT Client in Python - OpenHAB

# Dependencies
* [Python3](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/)
* [Paho-MQTT](https://eclipse.org/paho/clients/python/)
* [VirtualENV](https://virtualenv.pypa.io/en/stable/)

# Installation
To make it simple, we work in a virtual machine.

## OpenHAB
 Openhab will ack as the MQTT server and will display all the data he received from the MQTT client.
 For more  information on How To Install OpenHAB, [please refer to the doc](https://github.com/openhab/openhab/wiki/Ubuntu-on-x64)
### Configuration
* Config file `{INSTALLATION_FOLDER}/configuration/openhab.cfg` :

  * Persistance :
```
mqtt-persistence:broker=openhab
```
  * MQTT Transport :
```
mqtt:openhab.url=tcp://localhost:1883
```
* Item `{INSTALLATION_FOLDER}/configuration/item/demo.item`:

You can change the topics for what you want (ex: `paho/temparature`)
```
Number mqttsw1                  "temp [%.1f °C]" {mqtt="<[openhab:paho/temperature:state:default]"}
```
* Sitemap `{INSTALLATION_FOLDER}/configuration/sitemap/demo.sitemap`:
```
sitemap demo label="Main Menu"
{
        Frame label="MQTT" {
                Text item=mqttsw1
        }
}
```
### Mosquitto
During the installation of openhab, you will be ask to install.
In the config file `/etc/mosquitto/mosquitto.conf` you need to add this line :
`allow_anonymous = true`

Command that may help you to diagnotic issue with MQTT :

Subscribe to topics : `mosquitto_sub -d -t paho/temperature`

Send Msg to topics : `mosquitto_pub -d -t paho/temperature -m "18"`
## Client
Clone the branch :
`git clone https://github.com/gzsierra/pytt/`
`git checkout 180`
### Pip
For installation, [please see the doc](https://pip.pypa.io/en/stable/)
### Paho-MQTT
For installation, [please see the doc](https://eclipse.org/paho/clients/python/)
### VirtualENV (optional)
For installation, [please see the doc](https://virtualenv.pypa.io/en/stable/)

### Usage
Entry file format must be : `[TIME] [VALUE]`
ex: `timeX 18`

To execute the script : `python pytt.py test.txt`

# LICENCE
MIT
