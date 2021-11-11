FROM ubuntu:16.04
MAINTAINER Dieter Hsu "dieterplex@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV OPENGROK_INSTANCE_BASE /opengrok
ENV TERM xterm-color
ADD readonly_configuration.xml /etc/readonly_configuration.xml

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
                    openjdk-8-jre-headless tomcat8 inotify-tools \
                    exuberant-ctags git subversion mercurial curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# stable version
RUN mkdir /opengrok && curl -Lo - https://java.net/projects/opengrok/downloads/download/opengrok-0.12.1.5.tar.gz | tar zxvf - -C /opengrok --strip-components=1

# build latest from source and add relative old perforce binary
#COPY opengrok-0.13.tar.gz /tmp/
#RUN mkdir /opengrok && tar zxvf /tmp/opengrok-0.13.tar.gz -C /opengrok --strip-components=1
ADD http://filehost.perforce.com/perforce/r15.2/bin.linux26x86_64/p4 /usr/local/bin/p4
RUN chmod +x /usr/local/bin/p4

ADD run.sh /rungrok
ENTRYPOINT ["/rungrok"]

EXPOSE 8080
