FROM python:3.6.0

RUN apt-get -y upgrade
RUN apt-get -y update

RUN apt-get -y install nginx

RUN ln -s /srv/www/memex/memex/docker/server/memex_nginx.conf /etc/nginx/sites-enabled/

# add requirements.txt to the image
ADD requirements.txt /srv/www/memex/memex/requirements.txt

# set working directory to /memex/memex
WORKDIR /srv/www/memex/memex

# install python dependencies
RUN pip install -r requirements.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser
