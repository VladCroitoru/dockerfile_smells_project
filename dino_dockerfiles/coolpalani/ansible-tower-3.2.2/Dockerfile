# Ansible Tower Dockerfie

FROM ubuntu:16.04

MAINTAINER Palanisamy

ENV TOWER_VERSION=3.2.2
ENV PACKAGENAME=ansible-tower-setup-${TOWER_VERSION}

# Install tower

RUN apt-get update && \
	apt-get install -y \ 
		curl \
		iproute2 \
		locales \
		nano \
		software-properties-common \
		sudo 

RUN apt-add-repository ppa:ansible/ansible &&\
	mkdir -p /tmp/towersetup &&\
	cd /tmp/towersetup &&\
	curl -SOL https://releases.ansible.com/ansible-tower/setup/${PACKAGENAME}.tar.gz &&\
	tar -xvf ${PACKAGENAME}.tar.gz 

ADD inventory /tmp/towersetup/${PACKAGENAME}/

RUN locale-gen en_US
RUN locale-gen en_US.UTF-8

RUN cd /tmp/towersetup/${PACKAGENAME} \
	&& ./setup.sh

# Our stuff

COPY start /
RUN chmod +x ./start

RUN mkdir -p /certs

# VOLUME ${PG_DATA}
VOLUME /certs

VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG no_proxy

EXPOSE 443 80

CMD ["/start"]

RUN echo deleteme > /firstboot.flg

RUN apt install -y python-pip &&\
	pip install ansible-tower-cli &&\
	tower-cli config host localhost  &&\
	tower-cli config username admin  &&\
	tower-cli config password redhatcloud!

ENV TOWER_INIT_SCM_URL not_set
