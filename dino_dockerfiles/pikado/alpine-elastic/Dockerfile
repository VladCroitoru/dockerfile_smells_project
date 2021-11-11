FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade system
RUN apk --no-cache upgrade

# Install Java
RUN apk --no-cache add openjdk8

# Install tools
RUN apk --no-cache add curl

# Install and configure Elasticsearch
ENV ES_VERSION 2.3.2
ENV ES_USER elasticsearch
ENV ES_HOME /usr/local/elasticsearch
RUN curl -s https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ES_VERSION/elasticsearch-${ES_VERSION}.tar.gz | tar xz -C /usr/local
RUN adduser -D $ES_USER && ln -s $ES_HOME-$ES_VERSION $ES_HOME && chown -R $ES_USER: $ES_HOME*
USER $ES_USER
RUN sed -i 's/^# \(network.host:\)\( 192.168.0.1\)/\1 0.0.0.0/g' $ES_HOME/config/elasticsearch.yml
RUN $ES_HOME/bin/plugin install mobz/elasticsearch-head

# If you use Proxy replace previous command by this:
# RUN $ES_HOME/bin/plugin -DproxyHost=proxyva.casden.fr -DproxyPort=8080 install mobz/elasticsearch-head

# Set default command
CMD $ES_HOME/bin/elasticsearch
EXPOSE 9200 9300
