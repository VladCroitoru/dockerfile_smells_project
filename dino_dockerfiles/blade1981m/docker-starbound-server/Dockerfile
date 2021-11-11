FROM ubuntu:latest

MAINTAINER blade1981m <blade1981m@gmail.com>

VOLUME /starbound

COPY start.sh /start.sh

RUN apt-get update
RUN apt-get install lib32gcc1 wget libpng12-0 -y
RUN apt-get install lib32z1
RUN mkdir -p /starbound
RUN wget -o /tmp/steamcmd.tar.gz https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
RUN tar zxvf steamcmd_linux.tar.gz
RUN rm steamcmd_linux.tar.gz
RUN chmod +x /steamcmd.sh /start.sh

EXPOSE 21025
EXPOSE 20126

CMD /start.sh
