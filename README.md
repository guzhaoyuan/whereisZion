# whereisZion

This is a web application using flask and mqtt to show the position of Zion.

Find Zion's position in [whereis.guzhaoyuan.com](http://whereis.guzhaoyuan.com).

## how it works

- server host website indicating position of Zion
- server check domain of iPhone in CMU to find Zion in school, send mqtt message to notify server itself
- router at home LAN check domain of iPhone at Home to find Zion at home, send mqtt message to notify server
- server run mqtt to receive position info from router and server itself, update web

## files

- home.sh, run by router, check if my devices are at home, send info to server
- atSchool.py, run by server, check if my devices are at school, send info to server
- domain.py, contain domain name of my devices
- whereisZion.py, run by server, host web, receive mqtt message and change web content.

## TODO

- [x] everything
- [x] root router with openWRT
- [ ] write into database and use as reference
- [ ] encrypt mosquitto connection ssl
- [ ] ban mosquitto msg from other ip
- [ ] reverse error check of position detector if server not receive position report for a long time
- [ ] use invisible ink to debug


## Useful link

[Deploy Steps](https://github.com/guzhaoyuan/whereisZion/wiki/How-to-Deploy-whereisZion)

DO tutorial for [secure mqtt](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04)