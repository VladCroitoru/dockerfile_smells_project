FROM ubuntu:13.10
MAINTAINER Andrei Serdeliuc, andrei@apikot.com

RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y wget openjdk-7-jre-headless curl unzip git subversion mercurial

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN wget -O /tmp/go-server.deb http://download01.thoughtworks.com/go/13.4.1/ga/go-server-13.4.1-18342.deb
RUN dpkg -i /tmp/go-server.deb
RUN rm /tmp/go-server.deb

EXPOSE 8153
EXPOSE 8154

CMD ["/etc/init.d/go-server", "start"]
CMD /etc/init.d/go-server start && tail -f /var/log/go-server/go-server.log
