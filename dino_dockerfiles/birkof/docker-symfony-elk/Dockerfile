FROM java:8

MAINTAINER Daniel STANCU <birkof@birkof.ro>

ENV DEBIAN_FRONTEND noninteractive

# Update system repositories
RUN apt-get -y update

# Install apt-utils
RUN apt-get -y --force-yes install apt-utils

# Upgrade system
RUN apt-get -y dist-upgrade

RUN apt-get install --no-install-recommends -y supervisor

# Download and install the Public Signing Key:
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -

# Elasticsearch & Logstash repos
RUN \
    echo "deb http://packages.elastic.co/logstash/2.3/debian stable main" | tee -a /etc/apt/sources.list \
    && echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list \
    && echo "deb http://packages.elastic.co/kibana/4.5/debian stable main" | tee -a /etc/apt/sources.list \
    && apt-get update

# Elasticsearch
RUN \
    apt-get install --no-install-recommends -y elasticsearch \
    && sed -i 's/^# cluster.name:.*$/cluster.name: symfony/g' /etc/elasticsearch/elasticsearch.yml \
    && sed -i 's/^# path.data:.*$/path.data: \/tmp\/elasticsearch/g' /etc/elasticsearch/elasticsearch.yml \
    && sed -i 's/^#MAX_MAP_COUNT=.*$/MAX_MAP_COUNT=/g' /etc/default/elasticsearch
ADD supervisor/conf.d/elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

# Logstash
RUN apt-get install --no-install-recommends -y logstash
ADD supervisor/conf.d/logstash.conf /etc/supervisor/conf.d/logstash.conf

# Configs & patterns
ADD logstash/conf.d /etc/logstash/conf.d
ADD logstash/patterns /opt/logstash/patterns

# Logstash plugins
RUN /opt/logstash/bin/logstash-plugin install logstash-filter-translate

# Kibana
RUN apt-get install --no-install-recommends -y kibana
ADD supervisor/conf.d/kibana.conf /etc/supervisor/conf.d/kibana.conf

# Clean up the mess
RUN apt-get remove --purge -y \
        apt-utils \
    && apt-get autoclean \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Exposed port/s (web interface)
EXPOSE 5601 9200

# Environment variables
ENV PATH /opt/logstash/bin:$PATH

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]
