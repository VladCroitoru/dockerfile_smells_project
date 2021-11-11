FROM openjdk:16-jdk-buster

MAINTAINER BlueTooth

COPY ./init_server.sh /
RUN chmod +x /init_server.sh && \
apt-get update && \
apt-get -y install wget && \
rm -rf /var/lib/apt/lists/* && \
mkdir /data

WORKDIR /data
VOLUME /data

EXPOSE 25565

CMD /init_server.sh
