# Dockerfile for ELK stack
# Elasticsearch 1.7.1, Logstash 1.5.4, Kibana 4.1.1

# Build with:
# docker build -t <repo-user>/elk .

# Run with:
# docker run -p 5601:5601 -p 9200:9200 -p 5000:5000 -it --name elk <repo-user>/elk

FROM phusion/baseimage
MAINTAINER Sebastien Pujadas http://pujadas.net
ENV REFRESHED_AT 2015-08-15

###############################################################################
#                                INSTALLATION
###############################################################################

### install Elasticsearch

RUN \
    apt-get update \
        -qq \
    && apt-get install \
        -qq \
        --yes \
        --no-install-recommends \
        --no-install-suggests \
    curl \
    python-software-properties \
    software-properties-common \

# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Borrow gosu setup code from the docker-library Elasticsearch image found here:
# https://github.com/docker-library/elasticsearch/blob/master/1.5/Dockerfile
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
        && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
        && gpg --verify /usr/local/bin/gosu.asc \
        && rm /usr/local/bin/gosu.asc \
        && chmod +x /usr/local/bin/gosu

# Add Java.
RUN \
  echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
  && add-apt-repository -y ppa:webupd8team/java \
  && apt-get update \
       -qq \
  && apt-get install \
       -qq \
       -y oracle-java7-installer=7u80+7u60arm-0~webupd8~1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/oracle-jdk7-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

# Install Elasticsearch.
ENV ES_PKG_NAME elasticsearch-1.7.1
RUN \
  cd / \
  && wget https://download.elasticsearch.org/elasticsearch/elasticsearch/${ES_PKG_NAME}.tar.gz \
       --no-verbose \
  && tar xvzf $ES_PKG_NAME.tar.gz \
  && rm -f $ES_PKG_NAME.tar.gz \
  && mv /$ES_PKG_NAME /elasticsearch

# Set up default config.
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml

### install Logstash

ENV LOGSTASH_HOME /opt/logstash
ENV LOGSTASH_PACKAGE logstash-1.5.4.tar.gz

RUN mkdir ${LOGSTASH_HOME} \
 && curl -O https://download.elasticsearch.org/logstash/logstash/${LOGSTASH_PACKAGE} \
 && tar xzf ${LOGSTASH_PACKAGE} -C ${LOGSTASH_HOME} --strip-components=1 \
 && rm -f ${LOGSTASH_PACKAGE} \
 && groupadd -r logstash \
 && useradd -r -s /usr/sbin/nologin -d ${LOGSTASH_HOME} -c "Logstash service user" -g logstash logstash \
 && chown -R logstash:logstash ${LOGSTASH_HOME} \
 && mkdir -p /var/log/logstash /etc/logstash/conf.d

ADD ./logstash-init /etc/init.d/logstash
RUN sed -i -e 's#^LS_HOME=$#LS_HOME='$LOGSTASH_HOME'#' /etc/init.d/logstash \
 && chmod +x /etc/init.d/logstash

### install Kibana

ENV KIBANA_HOME /opt/kibana
ENV KIBANA_PACKAGE kibana-4.1.1-linux-x64.tar.gz

RUN mkdir ${KIBANA_HOME} \
 && curl -s -O https://download.elasticsearch.org/kibana/kibana/${KIBANA_PACKAGE} \
 && tar xzf ${KIBANA_PACKAGE} -C ${KIBANA_HOME} --strip-components=1 \
 && rm -f ${KIBANA_PACKAGE} \
 && groupadd -r kibana \
 && useradd -r -s /usr/sbin/nologin -d ${KIBANA_HOME} -c "Kibana service user" -g kibana kibana \
 && chown -R kibana:kibana ${KIBANA_HOME}

ADD ./kibana-init /etc/init.d/kibana
RUN sed -i -e 's#^KIBANA_HOME=$#KIBANA_HOME='$KIBANA_HOME'#' /etc/init.d/kibana \
 && chmod +x /etc/init.d/kibana

###
# Plugins
###

# http-basic plugin.
ENV HB_VERSION=1.5.0
ENV HTTP_BASIC_URL https://github.com/Asquera/elasticsearch-http-basic/releases/download/v${HB_VERSION}/elasticsearch-http-basic-${HB_VERSION}.jar
RUN /elasticsearch/bin/plugin \
  --url $HTTP_BASIC_URL \
  --install http-basic \
  --silent

# mapper-attachments plugin.
ENV MA_VERSION=2.7.0
RUN /elasticsearch/bin/plugin \
  install elasticsearch/elasticsearch-mapper-attachments/${MA_VERSION} \
  --silent

# elasticsearch-cloud-aws plugin.
ENV CA_VERSION=2.7.0
RUN /elasticsearch/bin/plugin install \
  elasticsearch/elasticsearch-cloud-aws/${CA_VERSION} \
  --silent

# marvel plugin
ENV MARVEL_VERSION=latest
RUN /elasticsearch/bin/plugin install \
  elasticsearch/marvel/${MARVEL_VERSION} \
  --silent

###############################################################################
#                               CONFIGURATION
###############################################################################

### configure Elasticsearch

ADD ./elasticsearch.yml /elasticsearch/config/elasticsearch.yml

### configure Logstash

# cert/key
RUN mkdir -p /etc/pki/tls/certs && mkdir /etc/pki/tls/private
ADD ./logstash-forwarder.crt /etc/pki/tls/certs/logstash-forwarder.crt
ADD ./logstash-forwarder.key /etc/pki/tls/private/logstash-forwarder.key

# filters
ADD ./01-syslog-input.conf /etc/logstash/conf.d/01-lumberjack-input.conf
ADD ./10-syslog.conf /etc/logstash/conf.d/10-syslog.conf
ADD ./11-nginx.conf /etc/logstash/conf.d/11-nginx.conf
ADD ./30-lumberjack-output.conf /etc/logstash/conf.d/30-lumberjack-output.conf

# patterns
ADD ./nginx.pattern ${LOGSTASH_HOME}/patterns/nginx
RUN chown -R logstash:logstash ${LOGSTASH_HOME}/patterns

###############################################################################
#                                   START
###############################################################################

RUN touch /.firstrun
ADD ./start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

EXPOSE 5601 9200 9300 5000
VOLUME /data

CMD [ "/usr/local/bin/start.sh" ]
