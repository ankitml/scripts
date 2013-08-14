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

# git install
sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev  git

#Django Install
sudo apt-get install python-pip
sudo pip install Django

#Django deployment
sudo apt-get install libapache2-mod-wsgi
sudo pip install django-tinymce django-localflavor PIL south

#Python packages
sudo apt-get install python-mysqldb python-tk python-beautifulsoup python-requests 
