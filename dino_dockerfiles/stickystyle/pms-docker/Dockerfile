FROM plexinc/pms-docker:plexpass

MAINTAINER Ryan Parrish <ryan@stickystyle.net>

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /opt

ADD . . 

RUN /opt/setup.sh 
