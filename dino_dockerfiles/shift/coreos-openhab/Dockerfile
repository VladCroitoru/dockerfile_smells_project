# Dockerfile for OpenHab 1.5

FROM ubuntu:14.04

MAINTAINER Vincent Palmer <shift-docker-openhab@someone.section.me>

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list

RUN DEBIAN_FRONTEND='noninteractive' apt-get update && apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/java -y

RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y oracle-java7-installer curl unzip

RUN (mkdir -p /opt/openhab/zips; cd /opt/openhab && curl -L https://github.com/openhab/openhab/releases/download/v1.5.0/distribution-1.5.0-runtime.zip -o zips/runtime.zip && unzip zips/runtime.zip && chmod u+x *.sh)
RUN (mkdir -p /opt/openhab/zips; cd /opt/openhab/addons && curl -L https://github.com/openhab/openhab/releases/download/v1.5.0/distribution-1.5.0-addons.zip -o ../zips/addons.zip && unzip ../zips/addons.zip)
RUN rm -rf /opt/openhab/zips

VOLUME /opt/openhab/configurations

EXPOSE 8080 8443

ENTRYPOINT ["/opt/openhab/start.sh"]
