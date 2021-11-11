FROM ubuntu:trusty
MAINTAINER jengelhardt211@gmail.com

RUN apt-get update &&\
    apt-get install -y pcp supervisor

ADD supervisor.conf /etc/supervisor/supervisord.conf

EXPOSE 44321 44322

CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
