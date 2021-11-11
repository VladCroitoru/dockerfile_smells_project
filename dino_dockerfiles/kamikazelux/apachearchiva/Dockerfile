FROM java:7u65

MAINTAINER Mike DE DOOD

ENV ARCHIVA_VERSION 2.2.0
ENV ARCHIVA_BASE /var/archiva

RUN curl -sSLo /tmp/apache-archiva-$ARCHIVA_VERSION-bin.tar.gz http://apache.mirrors.tds.net/archiva/$ARCHIVA_VERSION/binaries/apache-archiva-$ARCHIVA_VERSION-bin.tar.gz \
  && tar -xf /tmp/apache-archiva-$ARCHIVA_VERSION-bin.tar.gz --directory /opt \
  && rm /tmp/apache-archiva-$ARCHIVA_VERSION-bin.tar.gz

RUN adduser archiva

WORKDIR /opt/apache-archiva-$ARCHIVA_VERSION

RUN sed -i "/set.default.ARCHIVA_BASE/c\set.default.ARCHIVA_BASE=$ARCHIVA_BASE" conf/wrapper.conf
RUN mkdir -p $ARCHIVA_BASE/logs $ARCHIVA_BASE/data $ARCHIVA_BASE/temp $ARCHIVA_BASE/conf
RUN mv conf/* $ARCHIVA_BASE/conf
RUN chown -R archiva:archiva $ARCHIVA_BASE

# temp fix because ARCHIVA_BASE is not use by archiva :(
RUN rmdir logs conf temp
RUN ln -s $ARCHIVA_BASE/logs logs
RUN ln -s $ARCHIVA_BASE/conf conf
RUN ln -s $ARCHIVA_BASE/data data
RUN ln -s $ARCHIVA_BASE/temp temp

VOLUME /var/archiva
USER archiva

EXPOSE 8080
CMD bin/archiva console
