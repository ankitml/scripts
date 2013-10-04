#!/bin/sh
content=$(wget http://bkp.rigvee.com/ -q -O -)
Date=$(date +"%d-%m-%y")
echo $content >> log/DB_bkp@$Date.log.html
