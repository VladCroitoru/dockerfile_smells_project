FROM java:8

ENV DEBIAN_FRONTEND noninteractive
ENV ES_SKIP_SET_KERNEL_PARAMETERS true

RUN apt-get update && \
    apt-get install --no-install-recommends -y supervisor wget apt-transport-https && \
    apt-get clean

# ELK
RUN \
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    rm -f /etc/apt/sources.list.d/* && \
    if ! grep "elastic" /etc/apt/sources.list; then echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" >> /etc/apt/sources.list;fi && \
    apt-get update && \
    apt-get install --no-install-recommends -y elasticsearch logstash kibana && \
    apt-get clean && \
    sed -i '/#cluster.name:.*/a cluster.name: logstash' /etc/elasticsearch/elasticsearch.yml && \
    sed -i '/#path.data: \/path\/to\/data/a path.data: /data' /etc/elasticsearch/elasticsearch.yml && \
    sed -i '/#path.logs: \/path\/to\/logs/a path.logs: /var/log/elasticsearch' /etc/elasticsearch/elasticsearch.yml && \
    sed -i 's/#server\.port: 5601/server.port: 5601/' /etc/kibana/kibana.yml && \
    sed -i 's/#server\.host: "localhost"/server.host: 0\.0\.0\.0/' /etc/kibana/kibana.yml && \
    sed -i 's/#logging.dest: stdout/logging.dest: \/var\/log\/kibana\/kibana\.log/' /etc/kibana/kibana.yml

# Logstash plugins
RUN /usr/share/logstash/bin/logstash-plugin install logstash-filter-translate

ADD etc/supervisor/conf.d/ /etc/supervisor/conf.d/

RUN mkdir -p /var/log/elasticsearch && \
    mkdir /data && \
    mkdir -p /var/log/kibana && \
    chown elasticsearch:elasticsearch /var/log/elasticsearch && \
    chown elasticsearch:elasticsearch /data && \
    chown kibana:kibana /var/log/kibana

EXPOSE 5601 9200

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]
