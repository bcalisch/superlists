Provioning a new site
=====================

##Required packages:

* nginx
* Python 3
* pip
* virtualenv
* Git

e.g.,, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure
Assume we have a user account at /home/username

/home/username
|____sites
    |___SITENAME
       |___database
       |___source
       |___static
       |___virtualenv
