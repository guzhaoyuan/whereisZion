ping -c1 -w1 192.168.1.162
if [ $? -eq 0 ]
then 
  /root/script/presence.sh
else
  ping -c1 -w1 192.168.1.163
  if [ $? -eq 0 ]
  then
    /root/script/presence.sh
  else
    ping -c1 -w1 192.168.1.167
    if [ $? -eq 0 ]
    then
      /root/script/presence.sh
    else    
      /root/script/absence.sh
    fi
  fi
fi
