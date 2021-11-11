FROM webitel/freeswitch-base:vanilla
MAINTAINER Jovany Leandro G.C <dirindesa@neurotec.co>

RUN apt-get update && apt-get install -fy python vim
ADD https://github.com/plivo/plivoframework/raw/master/scripts/plivo_install.sh /plivo_install.sh
RUN bash /plivo_install.sh /plivo
COPY conf/default.conf /plivo/etc/plivo/default.conf
COPY conf/dialplan.xml /etc/freeswitch/dialplan/default.xml

COPY docker-entrypoint.d/plivoframework.sh /docker-entrypoint.d/plivoframework.sh

RUN mkdir -p /var/cache/freeswitch && chmod 777 /var/cache/freeswitch

RUN sed -i -r "s/PROTOCOL_SSLv3/PROTOCOL_SSLv23/g" /plivo/lib/python2.7/site-packages/gevent/ssl.py

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["freeswitch"]
