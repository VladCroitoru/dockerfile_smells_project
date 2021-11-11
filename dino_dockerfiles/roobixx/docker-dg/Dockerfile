FROM ubuntu
MAINTAINER Tim Fowler tim@roobixx.com


RUN echo deb http://archive.ubuntu.com/ubuntu/ precise main universe > /etc/apt/sources.list.d/precise.list
RUN apt-get update -q
RUN apt-get install -qy dansguardian squid

ADD ./bin /usr/local/sbin

EXPOSE 8080/tcp

CMD run