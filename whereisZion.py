from flask import Flask
from flask import render_template
import paho.mqtt.client as mqtt
import authentification

app = Flask(__name__)

atHome = 'n'
inSchool = 'n'


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
    if msg.topic == "schoool":
        global inSchool
        inSchool = msg.payload.decode('utf-8')
    if msg.topic == "home":
        global atHome
        atHome = msg.payload.decode('utf-8')


@app.route("/")
def hello():
    global atHome, inSchool
    return render_template('index.html', atHome=atHome, inSchool=inSchool)


# setup listener client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# connect to server
client.username_pw_set(authentification.servername, authentification.serverpassword)
client.connect(authentification.host, authentification.port)
client.loop_start()