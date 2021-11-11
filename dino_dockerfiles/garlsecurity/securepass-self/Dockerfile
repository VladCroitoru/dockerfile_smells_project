FROM centos:centos6
MAINTAINER Giuseppe Paterno' <gpaterno@gpaterno.com>

LABEL Description="SecurePass Self-Service Portal"

## Updates
RUN yum -y update

## Install EPEL stuffs
RUN rpm -ihv http://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

## Install pre/coreq
RUN yum -y install gcc python-pip python-virtualenv uwsgi-plugin-python uwsgi-router-http 

## Cleanup
RUN yum -y clean all

## Copy SecurePass
RUN mkdir -p /srv/securepass-self
COPY . /srv/securepass-self

## Install pip requisites
RUN virtualenv --system-site-packages /srv/securepass-self ; source /srv/securepass-self/bin/activate ; cd /srv/securepass-self ; pip install -r requirements.txt

EXPOSE 9090

WORKDIR /srv/securepass-self
CMD bash /srv/securepass-self/contrib/selfservice.sh
