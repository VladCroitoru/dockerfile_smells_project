# Dockerfile for ELK stack
# Elasticsearch, Logstash, Kibana 5.6.3

# Build with:
# docker build -t <repo-user>/elk .

# Run with:
# docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk <repo-user>/elk

FROM phusion/baseimage


###############################################################################
#                                INSTALLATION
###############################################################################

### install prerequisites (cURL, gosu, JDK)

ENV GOSU_VERSION 1.8

ARG DEBIAN_FRONTEND=noninteractive
RUN set -x \
 && apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends tzdata \
 && dpkg-reconfigure -f noninteractive tzdata \
 && apt-get install -qqy --no-install-recommends ca-certificates curl \
 && rm -rf /var/lib/apt/lists/* \
 && curl -L -o /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
 && curl -L -o /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
 && export GNUPGHOME="$(mktemp -d)" \
 && gpg --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
 && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
 && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
 && chmod +x /usr/local/bin/gosu \
 && gosu nobody true \
 && apt-get update -qq \
 && apt-get install -qqy openjdk-8-jdk \
 && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
 && apt-get clean \
 && set +x


ENV ELK_VERSION 5.6.3

# ADD ./limits.conf /etc/security/limits.conf
# RUN chmod +r /etc/security/limits.conf

### install Elasticsearch

ENV ES_VERSION ${ELK_VERSION}
ENV ES_HOME /opt/elasticsearch
ENV ES_PACKAGE elasticsearch-${ES_VERSION}.tar.gz
ENV ES_GID 441
ENV ES_UID 441

RUN mkdir ${ES_HOME} \
 && curl -O https://artifacts.elastic.co/downloads/elasticsearch/${ES_PACKAGE} \
 && tar xzf ${ES_PACKAGE} -C ${ES_HOME} --strip-components=1 \
 && rm -f ${ES_PACKAGE} \
 && groupadd -r elasticsearch -g ${ES_GID} \
 && useradd -r -s /usr/sbin/nologin -M -c "Elasticsearch service user" -u ${ES_UID} -g elasticsearch elasticsearch \
 && mkdir -p /var/log/elasticsearch /etc/elasticsearch /etc/elasticsearch/scripts /var/lib/elasticsearch \
 && chown -R elasticsearch:elasticsearch ${ES_HOME} /var/log/elasticsearch /var/lib/elasticsearch /etc/elasticsearch

ADD ./elasticsearch-init /etc/init.d/elasticsearch
RUN sed -i -e 's#^ES_HOME=$#ES_HOME='$ES_HOME'#' /etc/init.d/elasticsearch \
 && chmod +x /etc/init.d/elasticsearch


### install Logstash

ENV LOGSTASH_VERSION ${ELK_VERSION}
ENV LOGSTASH_HOME /opt/logstash
ENV LOGSTASH_PACKAGE logstash-${LOGSTASH_VERSION}.tar.gz
ENV LOGSTASH_GID 442
ENV LOGSTASH_UID 442

RUN mkdir ${LOGSTASH_HOME} \
 && curl -O https://artifacts.elastic.co/downloads/logstash/${LOGSTASH_PACKAGE} \
 && tar xzf ${LOGSTASH_PACKAGE} -C ${LOGSTASH_HOME} --strip-components=1 \
 && rm -f ${LOGSTASH_PACKAGE} \
 && groupadd -r logstash -g ${LOGSTASH_GID} \
 && useradd -r -s /usr/sbin/nologin -d ${LOGSTASH_HOME} -c "Logstash service user" -u ${LOGSTASH_UID} -g logstash logstash \
 && mkdir -p /var/log/logstash /etc/logstash/conf.d /var/lib/logstash \
 && chown -R logstash:logstash ${LOGSTASH_HOME} /var/log/logstash /etc/logstash /var/lib/logstash

ADD ./logstash-init /etc/init.d/logstash
RUN sed -i -e 's#^LS_HOME=$#LS_HOME='$LOGSTASH_HOME'#' /etc/init.d/logstash \
 && chmod +x /etc/init.d/logstash


### install Kibana

ENV KIBANA_VERSION ${ELK_VERSION}
ENV KIBANA_HOME /opt/kibana
ENV KIBANA_PACKAGE kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz
ENV KIBANA_GID 443
ENV KIBANA_UID 443

RUN mkdir ${KIBANA_HOME} \
 && curl -O https://artifacts.elastic.co/downloads/kibana/${KIBANA_PACKAGE} \
 && tar xzf ${KIBANA_PACKAGE} -C ${KIBANA_HOME} --strip-components=1 \
 && rm -f ${KIBANA_PACKAGE} \
 && groupadd -r kibana -g ${KIBANA_GID} \
 && useradd -r -s /usr/sbin/nologin -d ${KIBANA_HOME} -c "Kibana service user" -u ${KIBANA_UID} -g kibana kibana \
 && mkdir -p /var/log/kibana \
 && chown -R kibana:kibana ${KIBANA_HOME} /var/log/kibana

ADD ./kibana-init /etc/init.d/kibana
RUN sed -i -e 's#^KIBANA_HOME=$#KIBANA_HOME='$KIBANA_HOME'#' /etc/init.d/kibana \
    && chmod +x /etc/init.d/kibana

RUN mkdir -p /tmp/elasticsearch && chown -R elasticsearch:elasticsearch /tmp/elasticsearch \
    && mkdir -p /tmp/logstash && chown -R logstash:logstash /tmp/logstash \
    && mkdir -p /tmp/kibana && chown -R kibana:kibana /tmp/kibana


###############################################################################
#                               CONFIGURATION
###############################################################################

### configure Elasticsearch

ADD ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
ADD ./elasticsearch-log4j2.properties /etc/elasticsearch/log4j2.properties
ADD ./elasticsearch-jvm.options /opt/elasticsearch/config/jvm.options
ADD ./elasticsearch-default /etc/default/elasticsearch
RUN chmod -R +r /etc/elasticsearch


### configure Logstash

ADD ./logstash.yml /opt/logstash/config/logstash.yml
ADD ./logstash-jvm.options /opt/logstash/config/jvm.options
RUN chmod -R +r /opt/logstash/config

# filters
ADD ./00-kafka-input.conf /etc/logstash/conf.d/00-kafka-input.conf
ADD ./10-filter.conf /etc/logstash/conf.d/10-filter.conf
ADD ./11-filter.conf /etc/logstash/conf.d/11-filter.conf
ADD ./12-filter.conf /etc/logstash/conf.d/12-filter.conf
ADD ./30-output.conf /etc/logstash/conf.d/30-output.conf

# Fix permissions
RUN chmod -R +r /etc/logstash

### configure logrotate

ADD ./elasticsearch-logrotate /etc/logrotate.d/elasticsearch
ADD ./logstash-logrotate /etc/logrotate.d/logstash
ADD ./kibana-logrotate /etc/logrotate.d/kibana
RUN chmod 644 /etc/logrotate.d/elasticsearch \
 && chmod 644 /etc/logrotate.d/logstash \
 && chmod 644 /etc/logrotate.d/kibana


### configure Kibana

ADD ./kibana.yml ${KIBANA_HOME}/config/kibana.yml


###############################################################################
#                               PREPARE START
###############################################################################

ADD ./replace_ips.sh /usr/local/bin/replace_ips.sh
ADD ./start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/replace_ips.sh && \
  chmod +x /usr/local/bin/start.sh


###############################################################################
#                                XPACK INSTALLATION
###############################################################################

# ENV XPACK_VERSION 5.6.3
# ENV XPACK_PACKAGE x-pack-${XPACK_VERSION}.zip
#
# WORKDIR /tmp
# RUN curl -O https://artifacts.elastic.co/downloads/packs/x-pack/${XPACK_PACKAGE} \
#  && gosu elasticsearch ${ES_HOME}/bin/elasticsearch-plugin install \
#       -Edefault.path.conf=/etc/elasticsearch \
#       --batch file:///tmp/${XPACK_PACKAGE} \
#  && gosu kibana ${KIBANA_HOME}/bin/kibana-plugin install \
#       file:///tmp/${XPACK_PACKAGE} \
#  && rm -f ${XPACK_PACKAGE}
#
# RUN sed -i -e 's/curl localhost:9200/curl -u elastic:changeme localhost:9200/' \
#       -e 's/curl localhost:5601/curl -u kibana:paladin localhost:5601/' \
#       /usr/local/bin/start.sh


###############################################################################
#                                   START
###############################################################################

EXPOSE 5601 9200 9300 5044 9600
VOLUME /var/lib/elasticsearch

CMD [ "/usr/local/bin/start.sh" ]
