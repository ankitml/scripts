#!/bin/bash
sudo apt-get install vim ipython gcc g++ terminator git
sudo apt-get install php5 php5-mysql mysql-server-5.5  apache2
cd /var/
sudo chmod 777 www/
cd www
wget http://www.sourceforge.net/projects/phpmyadmin/files/phpMyAdmin/4.0.3/phpMyAdmin-4.0.3-all-languages.tar.bz2
tar -jxf phpMyAdmin-4.0.3-all-languages.tar.bz2 -C ./
rm -f phpMyAdmin-4.0.3-all-languages.tar.bz2
mv phpMyAdmin-4.0.3-all-languages pma
## This needs to be added to php.ini - "extension=mysqli.so"

#Django Install
sudo app-get install pip
pip install Django

#Python packages
sudo apt-get install python-mysqldb

