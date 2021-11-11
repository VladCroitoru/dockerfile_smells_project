FROM develar/java:latest
MAINTAINER Ludek Vesely <ludek.vesely@email.com>

ENV ES_VERSION 2.3.0

RUN apk add --update curl && \
	( curl -Lskj https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz | gunzip -c - | tar xf - ) && \
	mv /elasticsearch-$ES_VERSION /elasticsearch && \
	curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && chmod +x /usr/local/bin/gosu && \
	rm -rf $(find /elasticsearch | egrep "(\.(exe|bat)$|sigar/.*(dll|winnt|x86-linux|solaris|ia64|freebsd|macosx))") && \
	apk del curl && rm -rfv /var/cache/apk/* /tmp/* /var/tmp/* && \
 	cd /elasticsearch && bin/plugin install analysis-icu && bin/plugin install delete-by-query && \
 	bin/plugin install lmenezes/elasticsearch-kopf/2.0

ENV ES_CLUSTER_NAME=elastic \
	ES_NODE_LOCAL=true \
	ES_NUM_OF_SHARDS=1 \
	ES_NUM_OF_REPLICAS=0 \
	ES_PATH_DATA="/var/services/data/elasticsearch" \
	ES_PATH_LOG="/var/services/log/elasticsearch" \
	ES_LOG_LEVEL=INFO \
	ES_HEAP_SIZE=1G \
	ES_ADDITIONAL_CONFIG=""

ADD hunspell /elasticsearch/config/hunspell
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml
ADD logging.yml /elasticsearch/config/logging.yml
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["elasticsearch"]
EXPOSE 9200 9300

