# Dockerfile for ELK stack 5.x

# Build with:
# docker build -t <repo-user>/elk .

# Run with:
# docker run -d --name elk <repo-user>/elk
# or
# docker run -p 80:5601 -p 9200:9200 -p 5044:5044 -p 5000:5000 -it --name elk <repo-user>/elk

#FROM java:8-jre
# This image is officially deprecated in favor of the openjdk image,
# and will receive no further updates after 2016-12-31 (Dec 31, 2016)

# Change to OpenJDK
FROM openjdk:8-jre-alpine
# OS is Alpine 64bit

MAINTAINER Tuan Vo <vohungtuan@gmail.com>
# Reference Sebastien Pujadas http://pujadas.net

ENV ES_VERSION 5.5.2
ENV LOGSTASH_VERSION 5.5.2
ENV KIBANA_VERSION 5.5.2

ENV GOSU_VERSION 1.10
ENV TINI_VERSION v0.16.1

####################################################
########               Java              ###########
####################################################
# OpenJDK - Java 8

# They are defined in the base image openjdk:8-jre-alpine
# ENV JAVA_VERSION 8u92
# ENV JAVA_ALPINE_VERSION 8.92.14-r1
# ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
# ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

###############################################################################
#                                INSTALLATION
###############################################################################


####################################################
#########              GoSU              ###########
####################################################

### install gosu for easy step-down from root
### https://github.com/tianon/gosu/releases

RUN set -x \
    && apk add --no-cache --virtual .gosu-deps \
        dpkg \
        gnupg \
        openssl \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apk del .gosu-deps \
    && rm -rf /var/cache/apk/*
 
 ####################################################
#########              Tini              ###########
####################################################

 # grab tini for signal processing and zombie killing
 # https://github.com/krallin/tini/releases

# RUN set -x \
    # && apk add --no-cache --virtual .tini-deps \
        # dpkg \
        # gnupg \
        # openssl \
    # && wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" \
   # && wget -O /usr/local/bin/tini.asc "https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" \
   # && export GNUPGHOME="$(mktemp -d)" \
   # && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 6380DC428747F6C393FEACA59A84159D7001A4E5 \
   # && gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \
   # && rm -r "$GNUPGHOME" /usr/local/bin/tini.asc \
   # && chmod +x /usr/local/bin/tini \
   # && tini -h \
   # && apk del .tini-deps \
   # && rm -rf /var/cache/apk/*

# RUN set -x \
   # && apk add --update tini \
   # && rm -rf /var/cache/apk/* \
   # && tini -h   
# Tini is now available at /sbin/tini

####################################################
#########              Elasticsearch     ###########
####################################################

ENV ES_HOME /opt/elasticsearch

RUN set -x \
 && apk add --update bash \
        curl \
        tar \
        nodejs \
 && rm -rf /var/cache/apk/* \        
 && mkdir -p ${ES_HOME} \
 && addgroup elk \
 && adduser -D -S elk -s /bin/bash -h ${ES_HOME} -g "ELK service user" -G elk \
 && curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz \
 && tar xzf elasticsearch-${ES_VERSION}.tar.gz  -C ${ES_HOME} --strip-components=1 \
 && rm -rf elasticsearch-${ES_VERSION}.tar.gz \
 && for path in \
      ${ES_HOME}/data \
      ${ES_HOME}/logs \
      ${ES_HOME}/config \
      ${ES_HOME}/config/scripts \
      ; do \
      mkdir -p "$path"; \
    done \
 && chown -R elk:elk ${ES_HOME}


####################################################
#########              Logstash          ###########
####################################################


ENV LOGSTASH_HOME /opt/logstash

RUN set -x \
 && mkdir -p ${LOGSTASH_HOME} \
 && curl -L -O https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.tar.gz \
 && tar xzf logstash-${LOGSTASH_VERSION}.tar.gz -C ${LOGSTASH_HOME} --strip-components=1 \
 && rm -f logstash-${LOGSTASH_VERSION}.tar.gz \
 && chown -R elk:elk ${LOGSTASH_HOME}

 COPY logstash.conf ${LOGSTASH_HOME}/config/

####################################################
#########              Kibana            ###########
####################################################

ENV KIBANA_HOME /opt/kibana

RUN set -x \
 && mkdir -p ${KIBANA_HOME} \
 && curl -L -O https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz \
 && tar xzf kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz -C ${KIBANA_HOME} --strip-components=1 \
 && rm -f kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz \
 && chown -R elk:elk ${KIBANA_HOME}

 
# elasticsearch.url: 'http://elasticsearch:9200'
# ensure the default configuration is useful when using --link

# server.host: "0.0.0.0"
# ensure we can access kibana outside the host

# server.port: 5601
# ensure we can access kibana outside the host with port 5610

RUN set -x \
  # && sed -ri "s!^(\#\s*)?(elasticsearch\.url:).*!\2 'http://localhost:9200'!" ${KIBANA_HOME}/config/kibana.yml \
  # && grep -q 'localhost:9200' ${KIBANA_HOME}/config/kibana.yml \
  && sed -ri "s!^(\#\s*)?(server\.host:).*!\2 \"0\.0\.0\.0\"!" ${KIBANA_HOME}/config/kibana.yml \
  && grep -q '0.0.0.0' ${KIBANA_HOME}/config/kibana.yml \ 
  && sed -ri "s!^(\#\s*)?(server\.port:).*!\2 5601!" ${KIBANA_HOME}/config/kibana.yml \
  && grep -q '5601' ${KIBANA_HOME}/config/kibana.yml

# WORKDIR ${KIBANA_HOME}

###############################################################################
#                                   START
###############################################################################

ENV PATH ${JAVA_HOME}/bin:${ES_HOME}/bin:${LOGSTASH_HOME}/bin:${KIBANA_HOME}/bin:$PATH


# 9200 Elasticsearch HTTP JSON interface
# 9300 Elasticsearch TCP transport port
# 5044 Logstash Beats interface, receives logs from Beats such as Filebeat, Packetbeat
# 5601 Kibana web interface
EXPOSE 9200 9300 5044 5601

VOLUME ${ES_HOME}/data

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
 
ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [""]
