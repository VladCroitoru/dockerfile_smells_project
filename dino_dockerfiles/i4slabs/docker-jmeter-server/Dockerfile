FROM alpine:3.6

MAINTAINER i4slabs

ENV JMETER_VERSION 3.2
ENV JMETER_HOME /usr/local/apache-jmeter-${JMETER_VERSION}
ENV JMETER_BIN $JMETER_HOME/bin
ENV SERVER_PORT 1099
ENV IP 127.0.0.1
ENV RMI_LOCALPORT 1099
ENV LOCALHOSTNAME 127.0.0.1

RUN apk --update add openjdk8 tar unzip bash && \
    rm -rf /var/cache/apk/*

COPY dependencies /tmp/dependencies

RUN tar -xzf /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz -C /usr/local && \
    unzip -oq "/tmp/dependencies/plugins/*.zip" -d $JMETER_HOME && \
    rm -rf /tmp/dependencies

ENV PATH $PATH:$JMETER_BIN

WORKDIR $JMETER_HOME

EXPOSE $SERVER_PORT
EXPOSE $RMI_LOCALPORT

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
