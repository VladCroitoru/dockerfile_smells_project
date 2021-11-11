# Bind
#
# general nameserver based on bind9/ubuntu

FROM phusion/baseimage:latest
MAINTAINER dieKeuleCT <koehlmeier@gmail.com>

ENV HOME /root
ENV LANG en_US.UTF-8
RUN locale-gen en_US.UTF-8

RUN ln -s -f /bin/true /usr/bin/chfn

# Install packages
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install bind9 wget dnsutils
RUN wget http://www.webmin.com/jcameron-key.asc && apt-key add jcameron-key.asc
RUN echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list && echo "deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib" /etc/apt/sources.list && echo "Acquire::GzipIndexes \"false\"; Acquire::CompressionTypes::Order:: \"gz\";" > /etc/apt/apt.conf.d/docker-gzip-indexes
RUN apt-get update && apt-get -y install webmin
RUN apt-get clean

ADD run_bind9.sh /etc/service/named/run
ADD run_webmin.sh /etc/service/webmin/run
ADD update_pass.sh /etc/my_init.d/01_update_pass.sh

EXPOSE 10000
EXPOSE 53
EXPOSE 953

VOLUME ["/etc/bind","/var/lib/bind","/etc/webmin"]
CMD ["/sbin/my_init"]
