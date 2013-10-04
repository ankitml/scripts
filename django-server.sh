#ssh key
cd ~/.ssh && ssh-keygen
cat id_rsa.pub | pbcopy 
#put it in site

#git config
git config --global user.name "singlas"
git config --global user.email shashank.singla@gmail.com


#dont go in root


#vhost.conf in same directory as manage.py
WSGIScriptAlias /app /home/gitcode/legalczar/django/legalczar/wsgi.py

<Directory /home/gitcode/legalczar/django/legalczar>
<Files wsgi.py>
    Order allow,deny
    Allow from all
</Files>
</Directory>

#In wsgi.py below os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learned.settings") add (import sys)
sys.path.append('/home/gitcode/legalczar/django/legalczar')
sys.path.append('/home/gitcode/legalczar/django')

#In setting.py 
static_root = "/var/www/django_learned/"
static_url = "/django_learned/"

#in /etc/apache2/sites-available/default, add
Include /home/codes/learned/vhost.conf

#in /var/www/
mkdir django_learned

#for facebook
pip install pyoauth2
pip install facebook-sdk

#email server
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'shashank@refreshingsquares.com'
EMAIL_HOST_PASSWORD = '*******'
EMAIL_PORT = 587

#login redirect
LOGIN_URL = '/bb/accounts/login/'
LOGIN_REDIRECT_URL = "/bb/guide/page/1/"
ACCOUNT_LOGOUT_REDIRECT_URL = '/bb/accounts/login/'

#for scrappy
apt-get install python-dev libxml2 libxml2-dev libxslt-dev
pip install Scrapy

#for flask
pip install Flask

#to get apache user
ps aux | grep apache 

#in wsgi set os.chdir("/home/local/username/project/scrapy/modulename")
pip install PIL


#for restarting apache from python
#in /etc/sudoers add 2 lines
Cmnd_Alias RAPACHE = /etc/init.d/apache2                                                           
www-data ALL=NOPASSWD: RAPACHE

#then call
sudo /etc/init.d/apache2 reload