FROM ubuntu
MAINTAINER Atsushi Sasaki

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y supervisor
RUN apt-get install -y openssh-server
RUN apt-get install -y curl
RUN apt-get install -y zip
RUN apt-get install -y socat

RUN curl -L -O https://dl.bintray.com/mitchellh/consul/0.2.0_linux_amd64.zip
RUN unzip 0.2.0_linux_amd64.zip
RUN chmod +x consul
RUN mv consul /usr/local/bin 
RUN mkdir /etc/consul.d

RUN mkdir /var/run/sshd
RUN mkdir -p /var/log/supervisor

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD sshd.json /etc/consul.d/sshd.json
ADD socat.json /etc/consul.d/socat.json

RUN echo 'root:password' | chpasswd

EXPOSE 22 8300 8301 8302 8400 8500 8600
CMD ["/usr/bin/supervisord"]
