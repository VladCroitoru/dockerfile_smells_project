FROM elasticsearch:2.3.3

MAINTAINER sparklxb@163.com

WORKDIR /usr/share/elasticsearch

# Install Elasticsearch plug-ins
RUN ./bin/plugin install io.fabric8/elasticsearch-cloud-kubernetes/2.3.3

# Override elasticsearch.yml config, otherwise plug-in install will fail
ADD elasticsearch.yml ./config/elasticsearch.yml

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
