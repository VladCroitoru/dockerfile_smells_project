FROM debian:latest

MAINTAINER p4km9y

RUN apt-get update && apt-get install -y wget && \
    wget -q -O - https://repo.mosquitto.org/debian/mosquitto-repo.gpg.key | apt-key add - && \
    codename=`wget -q -O - http://ftp.debian.org/debian/dists/stable/Release | grep Codename | cut -d\  -f 2` && \
    wget -q -O /etc/apt/sources.list.d/mosquitto.list https://repo.mosquitto.org/debian/mosquitto-${codename}.list && \
    apt-get update && apt-get install -y mosquitto

RUN adduser --system --disabled-password --disabled-login mosquitto && \
    sed -i 's/^\(persistence\s*.*\)$/#\1/' /etc/mosquitto/mosquitto.conf && \
    echo "user mosquitto" >> /etc/mosquitto/mosquitto.conf

# 9001 websockets not configured
EXPOSE 1883 9001

ENTRYPOINT ["/usr/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]

