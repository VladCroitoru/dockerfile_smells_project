############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

FROM phusion/baseimage:0.9.18

MAINTAINER Maintaner Name

# Add the application resources URL
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y tar build-essential python python-dev python-pip

#RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

#RUN apt-get install -y python python-dev python-distribute python-pip

ADD resources/server /server

RUN pip install -r /server/requirements.txt

EXPOSE 80

VOLUME /config

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init"]

RUN mkdir /etc/service/cherrypy

ADD resources/cherrypy.sh /etc/service/cherrypy/run
