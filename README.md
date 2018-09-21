# whereisZion

## under development

this is a web application using flask and mqtt to show the position of Zion.

find Zion's position in whereis.guzhaoyuan.com.

## how it works

- server host website indicating position of Zion
- server check domain of iPhone in CMU to find Zion in school, send mqtt message to notify server itself
- router at home LAN check domain of iPhone at Home to find Zion at home, send mqtt message to notify server
- server run mqtt to receive position info from router and server itself, update web

## files

- atHome.py, run by router, check if iPhone is at home, send info to server
- inSchool.py, run by server, check if iPhone is in school, send info to server
- domain.py, contain domain name of iPhone
- whereisZion.py, run by server, host web, receive mqtt message and change web content.

## TODO

- [x] everything
- [ ] root router with openWRT
- [ ] encrypt mosquitto connection ssl
- [ ] reverse error check of position detector if server not receive position report for a long time
- [ ] use invisible ink to debug


## Useful link

DO tutorial for [secure mqtt](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04)