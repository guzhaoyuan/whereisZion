# check if Zion is in School
import authentification  # password file

import paho.mqtt.client as mqtt
import os


def ping():
    response = os.system("ping -c 1 -w 1 %s > /dev/null" % authentification.iphoneSchoolDomain)
    response &= os.system("ping -c 1 -w 1 %s > /dev/null" % authentification.ipadSchoolDomain)
    response &= os.system("ping -c 1 -w 1 %s > /dev/null" % authentification.macSchoolDomain)
    if response == 0:
        print("ping success")
    else:
        print("ping fail")
    return response


# publish position section
client = mqtt.Client()

# connect to server
client.username_pw_set(authentification.servername, authentification.serverpassword)
client.connect(authentification.host, authentification.port)

# publish msg
if ping() == 0:  # at home
    ret = client.publish("school", "y")
else:  # not at home
    ret = client.publish("school", "n")

client.disconnect()