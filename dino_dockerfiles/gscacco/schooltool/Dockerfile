FROM phusion/baseimage:0.9.15
MAINTAINER Gianluca Scacco <gianluca.scacco@gmail.com>
RUN add-apt-repository ppa:schooltool-owners/2.8
RUN apt-get update
RUN apt-get install -y schooltool
RUN sed -i 's/host = 127.0.0.1/host = 0.0.0.0/' /etc/schooltool/standard/paste.ini
RUN sed -i 's/exit 0/service schooltool start/' /etc/rc.local
# It seems to have no effect on image size!
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 7080
