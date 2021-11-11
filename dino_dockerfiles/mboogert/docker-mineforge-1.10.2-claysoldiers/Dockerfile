FROM debian:wheezy

MAINTAINER Marcel Boogert <marcel@mtdb.nlm>

RUN \
    apt-get -y update && \
    apt-get -y install openjdk-7-jre-headless wget

RUN wget -q https://github.com/mboogert/docker-mineforge-1.10.2-claysoldiers/upload/master/mineforge-1.10.2-claysoldiers.jar

WORKDIR /data
VOLUME /data

EXPOSE 25565

CMD echo eula=true > /data/eula.txt && java -jar /mineforge-1.10.2-claysoldiers.jar
