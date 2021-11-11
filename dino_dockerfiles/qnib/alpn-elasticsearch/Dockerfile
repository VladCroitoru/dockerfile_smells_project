FROM qnib/alpn-jre8

ARG ES_VER=2.4.1
ARG ES_URL=https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch
ENV ES_DATA_NODE=true \
    ES_MASTER_NODE=true \
    ES_HEAP_SIZE=512m \
    ES_NET_HOST=0.0.0.0 \
    ES_PATH_DATA=/opt/elasticsearch/data/ \
    ES_PATH_LOGS=/opt/elasticsearch/logs \
    ES_MLOCKALL=true
RUN apk --no-cache add curl nmap jq vim \
 && curl -sL ${ES_URL}/${ES_VER}/elasticsearch-${ES_VER}.tar.gz |tar xfz - -C /opt/ \
 && mv /opt/elasticsearch-${ES_VER} /opt/elasticsearch
VOLUME ["/opt/elasticsearch/logs", "/opt/elasticsearch/data/"]
RUN adduser -s /bin/bash -u 2000 -h /opt/elasticsearch -H -D elasticsearch \
 && echo "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/jdk/bin" >> /opt/elasticsearch/.bash_profile \
 && chown -R elasticsearch: /opt/elasticsearch
ADD etc/consul-templates/elasticsearch/elasticsearch.yml.ctmpl \
    etc/consul-templates/elasticsearch/logging.yml.ctmpl \
    etc/consul-templates/elasticsearch/elasticsearch.json.ctmpl \
    /etc/consul-templates/elasticsearch/
ADD opt/qnib/elasticsearch/bin/start.sh \
    opt/qnib/elasticsearch/bin/stop.sh \
    opt/qnib/elasticsearch/bin/register.sh \
    opt/qnib/elasticsearch/bin/healthcheck.sh \
    /opt/qnib/elasticsearch/bin/
ADD opt/qnib/elasticsearch/index-registration/settings/*.json /opt/qnib/elasticsearch/index-registration/settings/
ADD etc/supervisord.d/elasticsearch.ini \
    etc/supervisord.d/es-register.ini \
    /etc/supervisord.d/
ADD /etc/consul.d/elasticsearch.json /etc/consul.d/
RUN apk add --update python git bc \
 && curl -sLo /opt/es-backup-scripts.zip https://github.com/import-io/es-backup-scripts/archive/master.zip \
 && unzip -q -d /opt/ /opt/es-backup-scripts.zip \
 && rm -f /opt/es-backup-scripts.zip \
 && mv /opt/es-backup-scripts-master/ /opt/es-backup-scripts \
 && apk del git \
 && rm -rf /var/cache/apk/* /tmp/* \
 && mkdir -p /opt/qnib/elasticsearch/index-registration/mappings
HEALTHCHECK --interval=2s --retries=300 --timeout=1s \
 CMD /opt/qnib/elasticsearch/bin/healthcheck.sh
