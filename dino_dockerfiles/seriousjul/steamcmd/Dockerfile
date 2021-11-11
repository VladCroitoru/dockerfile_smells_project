FROM ubuntu:latest

MAINTAINER Julien Antony <jul.antony@gmail.com>
VOLUME /game

ENV login anonymous
ENV app_update 0

ADD install.sh /tmp
RUN /tmp/install.sh

CMD /root/steamcmd/steamcmd.sh +login $login +force_install_dir /game +app_update $app_update validate +quit