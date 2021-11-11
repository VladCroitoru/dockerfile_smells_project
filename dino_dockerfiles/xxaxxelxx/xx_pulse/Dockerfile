FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>

#RUN sed -e 's/$/ contrib non-free/' -i /etc/apt/sources.list 

RUN apt-get -qq -y update
#RUN apt-get -qq -y dist-upgrade

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq -y install mc
RUN apt-get -qq -y install curl
RUN apt-get -qq -y install libxml2-utils

# clean up
RUN apt-get clean

ENV UPDATE_ADMIN_PASS='updateadminpass'
ENV IC_ADMIN_PASS='icadminpass'
ENV IC_PORT=80
ENV IC_HOST=127.0.0.1
ENV LOOP_SEC=1
ENV LOADBALANCER_ADDR='192.168.90.29'
ENV MOUNTPOINT_LIST='dummy.mp3'
ENV BW_LIMIT=0
ENV LOAD_LIMIT=0

COPY *.sh /
RUN chmod 700 /*.sh

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
#CMD [ "bash" ]
