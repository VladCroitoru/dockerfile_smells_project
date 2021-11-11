FROM java:7

ADD scripts/run.sh /run.sh

RUN wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.4.tar.gz -O - | tar zxvf - && \
    mv elasticsearch-1.4.4 /elasticsearch && \
    /elasticsearch/bin/plugin -i mobz/elasticsearch-head && \
    /elasticsearch/bin/plugin -i lukas-vlcek/bigdesk && \
    /elasticsearch/bin/plugin -u https://github.com/viniciusccarvalho/elasticsearch-diego-discovery/releases/download/v1.0.0/diego-discovery-plugin-1.0.0-SNAPSHOT.zip -i diego

ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml


VOLUME ["/data", "/logs"]
EXPOSE 9200 9300
CMD ["/run.sh"]


