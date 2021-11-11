FROM ubuntu:xenial

RUN apt-get update -q && \
    apt-get upgrade -qy && \
    apt-get install -qy openjdk-8-jre-headless && \
    apt-get install -qy openssh-client && \
    apt-get clean

ADD ["http://dl.bintray.com/rundeck/rundeck-deb/rundeck-2.6.7-1-GA.deb", "/rundeck.deb"]

RUN dpkg -i /rundeck.deb && \
    rm -f /rundeck.deb
    
ADD launch.sh /launch.sh

RUN chmod +x "/launch.sh"
    
EXPOSE 4440

VOLUME  ["/etc/rundeck"]
VOLUME  ["/var/rundeck"]
VOLUME  ["/var/lib/rundeck"]
VOLUME  ["/var/log/rundeck"]

CMD ["/launch.sh"]
