FROM openjdk:7-jre-alpine
MAINTAINER Ian Duffy <ian@ianduffy.ie>

EXPOSE 8080
EXPOSE 4242
EXPOSE 2003
EXPOSE 2004

# Install curl
RUN apk add --update curl bash gettext && \
    rm -rf /var/cache/apk/*

RUN ln -s /usr/bin/envsubst /usr/sbin/envsubst

# Install kariosdb
RUN mkdir -p /opt \
  && cd /opt \
  && curl -L https://github.com/kairosdb/kairosdb/releases/download/v1.1.1/kairosdb-1.1.1-1.tar.gz | tar zxfp - \
  && curl -L https://github.com/kairosdb/kairos-carbon/releases/download/v1.0-1/kairos-carbon-1.0.tar.gz | tar zxfp -

ADD kairosdb.properties /tmp/kairosdb.properties
ADD runKairos.sh /runKairos.sh

ENTRYPOINT [ "/runKairos.sh" ]
