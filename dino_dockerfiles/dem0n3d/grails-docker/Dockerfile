FROM java:7

MAINTAINER Дмитрий Баранов <baranov@semograph.com>

ENV GRAILS_VERSION 2.4.4

WORKDIR /usr/lib/jvm

RUN wget https://github.com/grails/grails-core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \
    unzip grails-$GRAILS_VERSION.zip && \
    rm -rf grails-$GRAILS_VERSION.zip && \
    mv grails-$GRAILS_VERSION grails
  
ENV GRAILS_HOME /usr/lib/jvm/grails
ENV PATH $GRAILS_HOME/bin:$PATH
