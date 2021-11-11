FROM mamohr/centos-java
RUN rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch
ADD elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo
RUN yum -y install elasticsearch-5.5.2-1 sudo unzip && \
    yum -y clean all

ADD elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
ADD log4j2.properties /etc/elasticsearch/log4j2.properties
ADD jvm.options /etc/elasticsearch/jvm.options
ADD sudoers /etc/sudoers
USER root
RUN chown elasticsearch:elasticsearch /etc/elasticsearch/elasticsearch.yml && \
    mkdir /var/data && \
    chown elasticsearch:elasticsearch /var/data && \
    chmod -R 0777 /var/log/elasticsearch && \
    chmod -R 0777 /var/data && \
    /usr/share/elasticsearch/bin/elasticsearch-plugin  install -b https://distfiles.compuscene.net/elasticsearch/elasticsearch-prometheus-exporter-5.5.2.0.zip

COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
USER elasticsearch
EXPOSE 9200
ENTRYPOINT ["/docker-entrypoint.sh"]
