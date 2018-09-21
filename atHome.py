# check if Zion is at home
# this is script runs on openWRT

import authentification  # password file

import paho.mqtt.client as mqtt
import os


def on_publish():  # create function for callback
    print("position published \n")
    return


def ping():
    response = os.system("ping -q -c 1 %s > /dev/null" % authentification.iphoneHomeDomain)  # output is system dependent
    response &= os.system("ping -q -c 1 %s > /dev/null" % authentification.ipadHomeDomain)
    response &= os.system("ping -q -c 1 %s > /dev/null" % authentification.macHomeDomain)
    # response &= os.system("ping -q -c 1 %s > /dev/null" % authentification.pcHomeDomain)
    return response


# publish position section
client = mqtt.Client()
client.on_publish = on_publish

# connect to server
client.username_pw_set(authentification.routername, authentification.routerpassword)
client.connect(authentification.host, authentification.port)

# publish msg
if ping() == 0:  # at home
    ret = client.publish("home", "y")
else:  # not at home
    ret = client.publish("home", "n")

client.disconnect()
