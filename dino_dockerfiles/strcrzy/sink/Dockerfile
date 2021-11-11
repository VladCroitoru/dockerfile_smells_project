# strcrzy/sink
# a debian based docker image that includes:
#   - elasticsearch, logstash, kibana
#   - kibana dashboards for bro and suricata
# soon:
#   - logstash grok patterns for bro
#
# designed for use with strcrzy/sensor
#

FROM debian:jessie
MAINTAINER strcrzy, https://github.com/strcrzy

ENV KIBANA_VERSION 3.1.0
ENV LOGSTASH_VERSION 1.4.2
ENV SINCEDB_PATH /sink/.sincedb

RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && \
    chmod +x /usr/sbin/policy-rc.d

RUN apt-get -qq update && apt-get -qq install nginx wget supervisor \
    software-properties-common unzip

# elasticsearch
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch \
    | apt-key add -
RUN add-apt-repository \
    'deb http://packages.elasticsearch.org/elasticsearch/1.3/debian stable main'
RUN apt-get -qq update
RUN apt-get -qq install elasticsearch openjdk-7-jre-headless
ADD /etc/supervisor/conf.d/elasticsearch /etc/supervisor/conf.d/

# kibana/nginx
WORKDIR /opt/
ADD https://download.elasticsearch.org/kibana/kibana/kibana-$KIBANA_VERSION.tar.gz /opt/
RUN \
  tar xzf kibana-$KIBANA_VERSION.tar.gz && \
  rm kibana-$KIBANA_VERSION.tar.gz && \
  mkdir -p /var/www && \
  ln -s /opt/kibana-$KIBANA_VERSION /var/www/kibana && \
  sed -i 's/9200"/"+ window.location.port/g' /var/www/kibana/config.js

WORKDIR /etc/nginx/
RUN if ! grep "daemon off" nginx.conf ; \
    then sed -i '/worker_processes.*/a daemon off;' nginx.conf;fi
RUN rm sites-enabled/default && ln -s ../sites-available/kibana \
    sites-enabled/kibana
ADD etc/nginx/sites-available/kibana /etc/nginx/sites-available/
ADD /etc/supervisor/conf.d/nginx /etc/supervisor/conf.d/

#  kibana dashboards
ADD /opt/kibana/app/dashboards/bro-basic.json /opt/kibana-$KIBANA_VERSION/app/dashboards/
ADD /opt/kibana/app/dashboards/suricata.json /opt/kibana-$KIBANA_VERSION/app/dashboards/

# logstash
WORKDIR /opt/
RUN \
    apt-add-repository \
    'deb http://packages.elasticsearch.org/logstash/1.4/debian stable main' && \
    apt-get -qq update && \
    apt-get install logstash
ADD /etc/logstash/conf.d/bro.conf /etc/logstash/conf.d/
ADD /etc/logstash/conf.d/suricata.conf /etc/logstash/conf.d/
ADD /etc/supervisor/conf.d/logstash /etc/supervisor/conf.d/

ADD /etc/supervisor/supervisord.conf /etc/supervisor/
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


EXPOSE 80
ENTRYPOINT ["/usr/bin/supervisord"]
CMD ["-n", "-c", "/etc/supervisor/supervisord.conf"]