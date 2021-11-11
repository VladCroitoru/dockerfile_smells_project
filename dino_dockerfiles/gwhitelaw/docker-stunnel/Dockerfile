# stunnel Server
#
# VERSION 0.0.1

# Building from Ubuntu Trusty
FROM ubuntu:trusty

MAINTAINER George Whitelaw, g.whitelaw@gmail.com

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get -y install stunnel4

RUN sed -ir "s/ENABLED=0/ENABLED=1/" /etc/default/stunnel4

VOLUME ["/etc/stunnel"]

ADD conf/stunnel.conf /etc/stunnel/stunnel.conf
ADD conf/stunnel.cert /etc/stunnel/stunnel.cert
ADD conf/stunnel.key /etc/stunnel/stunnel.key
ADD run.sh /usr/bin/run
RUN chmod +x /usr/bin/run

EXPOSE 443

CMD ["/usr/bin/run"]
