from flask import Flask
from flask import render_template

import paho.mqtt.client as mqtt
import datetime
import authentification

app = Flask(__name__)

atHome = 'n'
atSchool = 'n'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.publish("topic", "server listener connect success")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home", 2)
    client.subscribe("school", 2)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Desconexion inesperada al servidor MQTT COD:[{0}]".format(str(rc)))


def on_message(client, userdata, msg):
    global atSchool, atHome
    if msg.topic == "school":
        atSchool = msg.payload.decode('utf-8')
        if atSchool == 'y':
            atHome = 'n'
    if msg.topic == "home":
        atHome = msg.payload.decode('utf-8')
        if atHome == 'y':
            atSchool = 'n'


@app.route("/")
def hello():
    global atHome, atSchool
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M")
    return render_template('index.html', atHome=atHome, atSchool=atSchool, date=date)


# setup listener client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# connect to server
client.username_pw_set(authentification.servername, authentification.serverpassword)
client.connect(authentification.host, authentification.port)
client.loop_start()