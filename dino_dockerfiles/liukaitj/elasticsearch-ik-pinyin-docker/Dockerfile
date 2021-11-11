# ElasticSearch docker with ik-pinyin support derived from https://github.com/hangxin1940/docker-elasticsearch-cn
FROM java:8-jre
MAINTAINER liukaitj <liukai.tci@gmail.com>

RUN wget -q http://github.com/liukaitj/elasticsearch-cn-out-of-box/archive/v1.6.0P.docker.zip && unzip -qq v1.6.0P.docker.zip && \
    mv /elasticsearch-cn-out-of-box-1.6.0P.docker /elasticsearch && \
    rm /elasticsearch/lib/sigar/*freebsd* && \
    rm /elasticsearch/lib/sigar/*solaris* && \
    rm /elasticsearch/lib/sigar/*winnt* && \
    rm /elasticsearch/bin/*.exe && \
    rm -rf /elasticsearch/bin/service && \
    rm -rf /elasticsearch/plugins/marvel && \
    rm v1.6.0P.docker.zip

RUN mkdir /data /logs

VOLUME ["/data", "/logs"]

ENV ES_HOME /elasticsearch

ADD docker-entrypoint.sh /elasticsearch/bin/docker-entrypoint.sh

RUN chmod +x /elasticsearch/bin/docker-entrypoint.sh && \
    chmod +x /elasticsearch/bin/elasticsearch

EXPOSE 9200 9300
CMD ["/elasticsearch/bin/docker-entrypoint.sh"]
