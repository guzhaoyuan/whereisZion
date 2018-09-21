# check if Zion is in School
import authentification  # password file

import paho.mqtt.client as mqtt
import os


def on_publish():  # create function for callback
    print("position published \n")
    pass


def ping():
    response = os.system("ping -q -c 1 %s > /dev/null" % authentification.iphoneSchoolDomain)  # output is system dependent
    response &= os.system("ping -q -c 1 %s > /dev/null" % authentification.ipadSchoolDomain)
    response &= os.system("ping -q -c 1 %s > /dev/null" % authentification.macSchoolDomain)
    # response &= os.system("ping -q -c 1 %s > /dev/null" % authentification.pcHomeDomain)
    return response


# publish position section
client = mqtt.Client()
client.on_publish = on_publish

# connect to server
client.username_pw_set(authentification.servername, authentification.serverpassword)
client.connect(authentification.host, authentification.port)

# publish msg
if ping() == 0:  # at home
    ret = client.publish("school", "y")
else:  # not at home
    ret = client.publish("school", "n")

client.disconnect()