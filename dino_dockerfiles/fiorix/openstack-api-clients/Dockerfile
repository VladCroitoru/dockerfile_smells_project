# VERSION 0.1
# AUTHOR:	Alexandre Fiori <fiorix@gmail.com>
# DESCRIPTION:	OpenStack command line API clients
# BUILD:	docker build --rm -t fiorix/openstack-client-api .

FROM ubuntu

RUN apt-get update
RUN apt-get install -y \
	build-essential \
	libssl-dev \
	libffi-dev \
	libyaml-dev \
	python-dev \
	python-setuptools \
	python-pip \
	python-virtualenv

RUN virtualenv /root/os
RUN bash -c 'source /root/os/bin/activate && pip install \
	netifaces \
	python-novaclient \
	python-neutronclient \
	python-glanceclient \
	python-heatclient'

RUN apt-get autoremove --purge -y build-essential .*-dev
RUN apt-get clean

COPY bash_profile /root/.bash_profile

CMD ["bash", "-l"]
