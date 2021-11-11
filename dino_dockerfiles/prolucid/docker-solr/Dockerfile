FROM phusion/baseimage
MAINTAINER Daniel Covello 
ENV DEBIAN_FRONTEND noninteractive

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ENV DISABLE_SSH 1
ENV SOLR_VERSION 6.1.0

# Install Java
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update && apt-get install -y openjdk-8-jdk unzip wget

ENV SOLR_USER solr
ENV SOLR_UID 8983

RUN groupadd -r -g $SOLR_UID $SOLR_USER && \
  useradd -r -u $SOLR_UID -g $SOLR_USER $SOLR_USER

RUN mkdir -p  /opt/solr  && \
  wget http://www-us.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz -O /opt/solr.tgz && \
  tar -C /opt/solr -xvf /opt/solr.tgz --strip-components=1 && \
  chown -R $SOLR_USER:$SOLR_USER /opt/solr 

RUN mkdir -p /etc/service/solr/
COPY start-solr.sh /etc/service/solr/run
RUN chmod +x /etc/service/solr/run

EXPOSE 8983

WORKDIR /opt/solr
