# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Stephane Jourdan "fasten@fastmail.fm"
ENV REFRESHED_AT 2015-04-02
RUN apt-get update -qq
RUN echo "deb http://apt.sourcefabric.org/ trusty main" >> /etc/apt/sources.list.d/airtime.list
RUN echo "deb http://archive.ubuntu.com/ubuntu/ precise multiverse" >> /etc/apt/sources.list.d/ubuntu-multiverse.list
RUN apt-get update -qq
RUN apt-get install -y sourcefabric-keyring --force-yes
RUN apt-get update -qq
RUN apt-get install -y airtime
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 443
