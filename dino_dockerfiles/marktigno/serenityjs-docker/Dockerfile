FROM centos:latest

LABEL maintainer="Mark Joseph R. Tigno" email="markj_tigno@hotmail.com"

RUN yum -y update; yum clean all; rm -rf /var/cache/yum
RUN yum -y install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum -y install epel-release
RUN yum -y install libappindicator
RUN yum -y install ./google-chrome-stable_current_*.rpm
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -
RUN yum -y install nodejs
RUN yum -y install java-1.8.0-openjdk
RUN yum -y install git
RUN yum -y install xorg-x11-server-Xvfb
RUN dbus-uuidgen > /etc/machine-id
RUN yum clean all; rm -rf /var/cache/yum
RUN mkdir -p /app
WORKDIR /app

RUN git clone https://github.com/marktigno/serenityjs-docker.git
WORKDIR /app/serenityjs-docker
RUN npm install
RUN chmod +x run-serenity