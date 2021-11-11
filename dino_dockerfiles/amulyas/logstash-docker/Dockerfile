FROM frodenas/java7
MAINTAINER Long Nguyen & Dr Nic Williams & Amulya Shamra

ENV DEBIAN_FRONTEND noninteractive

RUN \
# Elasticsearch
    wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    apt-key adv --keyserver pool.sks-keyservers.net --recv-keys 46095ACC8548582C1A2699A9D27D666CD88E42B4 && \
    if ! grep "elasticsearch" /etc/apt/sources.list; then echo "deb http://packages.elastic.co/elasticsearch/1.4/debian stable main" >> /etc/apt/sources.list;fi && \
    if ! grep "logstash" /etc/apt/sources.list; then echo "deb http://packages.elastic.co/logstash/1.4/debian stable main" >> /etc/apt/sources.list;fi && \
    if ! grep "curator" /etc/apt/sources.list; then echo "deb http://packages.elastic.co/curator/3/debian stable main" >> /etc/apt/sources.list;fi && \
    apt-get update && \
    apt-get install -y supervisor curl && \
    apt-get install -y elasticsearch && \
    apt-get install -y python-elasticsearch-curator && \
    apt-get install -y logstash && \
    apt-get clean && \
    sed -i '/#path.data: \/path\/to\/data/a path.data: /data' /etc/elasticsearch/elasticsearch.yml

#Add service config
ADD etc/supervisor/conf.d/elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf
ADD etc/supervisor/conf.d/logstash.conf /etc/supervisor/conf.d/logstash.conf
ADD etc/supervisor/conf.d/cron.conf /etc/supervisor/conf.d/cron.conf
ADD usr/share/elasticsearch/lib/elasticsearch-http-basic-1.5.1.jar /usr/share/elasticsearch/lib/elasticsearch-http-basic-1.5.1.jar
ADD usr/share/elasticsearch/bin/elasticsearch.in.sh /usr/share/elasticsearch/bin/elasticsearch.in.sh
RUN chmod +x /usr/share/elasticsearch/bin/*.sh

ADD /crontab.root /var/spool/cron/crontabs/root
RUN chown root:crontab /var/spool/cron/crontabs/root
RUN chmod 600 /var/spool/cron/crontabs/root
ADD etc/logstash/logstash.conf /etc/logstash/logstash.conf
ADD etc/kibana/config.js /opt/logstash/vendor/kibana/config.js

ADD scripts /scripts
RUN chmod +x /scripts/*.sh
RUN touch /.firstrun

RUN /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.4.2

ENTRYPOINT ["/scripts/run.sh"]
CMD [""]

EXPOSE 514
EXPOSE 9200
EXPOSE 9300

VOLUME ["/data"]
