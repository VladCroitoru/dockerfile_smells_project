FROM ubuntu:14.04.5
MAINTAINER Chris Salch <emeraldd.chris@gmail.com>
# Based on ctlc/serf by Lucas Carlson <lucas@rufy.com>

ENV DEBIAN_FRONTEND noninteractive

# Let's get serf
RUN apt-get update -q && apt-get install -qy build-essential git supervisor unzip

ADD https://releases.hashicorp.com/serf/0.8.0/serf_0.8.0_linux_amd64.zip serf.zip
RUN unzip serf.zip
RUN rm serf.zip
RUN mv serf /usr/bin/

ADD /start-serf.sh /start-serf.sh
ADD /run.sh /run.sh
ADD /supervisord-serf.conf /etc/supervisor/conf.d/supervisord-serf.conf

RUN chmod 755 /*.sh

EXPOSE 7946 7373

CMD ["/run.sh"]
