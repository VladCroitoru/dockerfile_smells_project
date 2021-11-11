FROM ubuntu 

MAINTAINER João Pedro < pedro.joao@gmail.com>
# make sure the package repository is up to date
# RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get update && apt-get -y install python-software-properties
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update && apt-get -y upgrade

# automatically accept oracle license
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
# and install java 7 oracle jdk
RUN apt-get -y install oracle-java7-installer && apt-get clean
RUN update-alternatives --display java
RUN echo "JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /etc/environment

RUN apt-get -y install unzip
RUN apt-get -y install subversion

RUN wget http://download.go.cd/gocd-deb/go-server-14.2.0-377.deb
RUN wget http://download.go.cd/gocd-deb/go-agent-14.2.0-377.deb
RUN dpkg -i go-server-*.deb
RUN dpkg -i go-agent-*.deb

EXPOSE 8153

RUN mkdir /opt/bin

RUN echo "/etc/init.d/go-server start" > /opt/bin/start_go.sh
RUN echo "/etc/init.d/go-server start" >> /opt/bin/start_go.sh
RUN chmod +x /opt/bin/start_go.sh

CMD /etc/init.d/go-server start && /etc/init.d/go-agent start && tail -f /var/log/syslog
 
