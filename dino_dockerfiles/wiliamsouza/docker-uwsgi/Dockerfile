# Uwsgi server generic image
#
# Version 0.1.0

FROM ubuntu:12.04

MAINTAINER Wiliam Souza <wiliamsouza83@gmail.com>

# base
ENV LANG en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales
RUN apt-get update

RUN apt-get install -y python-software-properties

# supervisor
RUN apt-get install supervisor -y
RUN update-rc.d -f supervisor disable

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# start script
ADD startup /usr/local/bin/startup
RUN chmod +x /usr/local/bin/startup

CMD ["/usr/local/bin/startup"]

# environment

# sources

# ppas

# dependencies
RUN apt-get install build-essential libpcre3-dev python python-dev wget -y

ADD sysctl.conf /etc/sysctl.conf

# setuptools
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
RUN python ez_setup.py

# pip
RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
RUN python get-pip.py

# uwsgi
RUN pip install uwsgi

VOLUME ["/etc/uwsgi", "/var/log/uwsgi", "/srv/project", "/srv/virtualenv"]

EXPOSE 8080
