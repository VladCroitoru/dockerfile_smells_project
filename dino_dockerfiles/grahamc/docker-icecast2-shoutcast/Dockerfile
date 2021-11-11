FROM ubuntu:14.04
MAINTAINER graham@grahamc.com

RUN sudo apt-get update
RUN sudo apt-get upgrade -y
RUN sudo apt-get install -y icecast2

ENV IC2_SOURCE_PASSWORD hackme
ENV IC2_RELAY_PASSWORD  hackme
ENV IC2_ADMIN_USER      admin
ENV IC2_ADMIN_PASSWORD  hackme

COPY config.xml /etc/icecast2/config.xml
COPY start.sh /start.sh

USER icecast2
VOLUME /logs
EXPOSE 8000 8001

CMD ["/usr/bin/icecast2", "-c", "/etc/icecast2/user-config.xml"]

