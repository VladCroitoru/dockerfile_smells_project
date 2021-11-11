FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>
RUN apt-get -qq -y update
#RUN apt-get -qq -y dist-upgrade

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq -y install icecast2

RUN apt-get -qq -y install telnet
RUN apt-get -qq -y install links
#RUN apt-get -qq -y install mc

RUN apt-get clean

COPY icecast_player.xml /etc/icecast2/icecast_player.xml
COPY icecast_proxy.xml /etc/icecast2/icecast_proxy.xml
RUN chown icecast2:icecast /etc/icecast2/icecast*.xml
RUN chmod 600 /etc/icecast2/icecast*.xml

#
#RUN chown -R icecast2:icecast /var/log/icecast2
#RUN chown -R icecast2:icecast /usr/share/icecast2
#

COPY ./entrypoint.sh /entrypoint.sh
RUN chown icecast2:icecast /entrypoint.sh
RUN chmod 700 /entrypoint.sh


ENV IC_SOURCE_PASS=myicsourcepass
ENV IC_RELAY_PASS=myicrelaypass
ENV IC_ADMIN_PASS=myicadminpass

ENV SIMULCAST_MASTER_SERVER_BBR=0.0.0.0
ENV CHANNELS_MASTER_SERVER_BBR=0.0.0.0
ENV SIMULCAST_MASTER_SERVER_TDY=0.0.0.0
ENV CHANNELS_MASTER_SERVER_TDY=0.0.0.0
ENV SIMULCAST_MASTER_SERVER_OW=0.0.0.0
ENV CHANNELS_MASTER_SERVER_OW=0.0.0.0
ENV SIMULCAST_PROXY_SERVER_BBR=0.0.0.0
ENV CHANNELS_PROXY_SERVER_BBR=0.0.0.0
ENV SIMULCAST_PROXY_SERVER_TDY=0.0.0.0
ENV CHANNELS_PROXY_SERVER_TDY=0.0.0.0
ENV SIMULCAST_PROXY_SERVER_OW=0.0.0.0
ENV CHANNELS_PROXY_SERVER_OW=0.0.0.0

ENV MASTER_SERVER_PORT=80
ENV PROXY_SERVER_PORT=8000

USER icecast2:icecast

EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "bash" ]
