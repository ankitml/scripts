#!/bin/bash
sudo apt-get install vim ipython gcc g++ terminator git
sudo apt-get install php5 php5-mysql mysql-server-5.5  apache2
cd /var/
sudo chmod 777 www/
cd www
tar -jxf phpMyAdmin-4.0.3-all-languages.tar.bz2 -C ./
rm -f phpMyAdmin-4.0.3-all-languages.tar.bz2
mv phpMyAdmin-4.0.3-all-languages pma
## This needs to be added to php.ini - "extension=mysqli.so"
