FROM phusion/passenger-nodejs:latest

RUN apt-get update && apt-get -y upgrade && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/service/nginx/down
RUN rm -f /etc/nginx/sites-enabled/default
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf
ADD setup.sh /etc/my_init.d/01_setup.sh
