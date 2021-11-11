FROM debian:jessie

MAINTAINER Jose Plana <jplana@gmail.com>

RUN apt-get update
RUN apt-get install -y graphite-carbon graphite-web supervisor

ADD configuration/services/supervisord/* /etc/supervisor/conf.d/
ADD configuration/services/carbon/carbon.conf /etc/carbon/carbon.conf
ADD configuration/services/carbon/storage-schemas.conf /etc/carbon/storage-schemas.conf

RUN su - _graphite -s /bin/sh -c "/usr/bin/graphite-manage migrate"

RUN chmod a+rwx /var/lib/graphite/whisper
VOLUME /var/lib/graphite/whisper

EXPOSE 2003 2004 8000
CMD supervisord --nodaemon -c /etc/supervisor/supervisord.conf
