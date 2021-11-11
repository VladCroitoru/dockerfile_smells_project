FROM debian:stretch-slim
MAINTAINER Alejandro Lazaro <virtualroot@gmail.com>

ENV GAME_TYPE ctf

RUN apt-get update \
 && apt-get install -y teeworlds-server pwgen \
 && apt-get clean all

COPY run.sh /run.sh

COPY dm.cfg /dm.cfg
COPY tdm.cfg /tdm.cfg
COPY ctf.cfg /ctf.cfg

RUN chmod +x /run.sh

EXPOSE 8303/udp
CMD ["/run.sh"]
