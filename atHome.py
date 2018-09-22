# check if Zion is at home
# this is script runs on openWRT

import authentification  # password file

import paho.mqtt.client as mqtt
import os


def ping():
    response = os.system("ping -c 1 -w 1 %s > /dev/null" % authentification.iphoneHomeDomain)  # output is system dependent
    response &= os.system("ping -c 1 -w 1 %s > /dev/null" % authentification.ipadHomeDomain)
    response &= os.system("ping -c 1 -w 1 %s > /dev/null" % authentification.macHomeDomain)
    if response == 0:
        print("ping success")
    else:
        print("ping fail")
    return response


# publish position section
client = mqtt.Client()

# connect to server
client.username_pw_set(authentification.routername, authentification.routerpassword)
client.connect(authentification.host, authentification.port)

# publish msg
if ping() == 0:  # at home
    ret = client.publish("home", "y")
else:  # not at home
    ret = client.publish("home", "n")

client.disconnect()
