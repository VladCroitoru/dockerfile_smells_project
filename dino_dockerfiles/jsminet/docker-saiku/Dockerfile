FROM java:6
MAINTAINER JS Minet

ADD http://meteorite.bi/downloads/saiku-latest.zip /home/root/

WORKDIR /home/root/

RUN unzip saiku-latest.zip && rm saiku-latest.zip

EXPOSE 8080

CMD ["saiku-server/start-saiku.sh"]
