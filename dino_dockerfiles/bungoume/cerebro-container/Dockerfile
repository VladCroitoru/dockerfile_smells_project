FROM openjdk:8-jre-alpine

ENV CEREBRO_VERSION 0.3.1

WORKDIR cerebro
RUN apk --no-cache --update add bash openssl tar && \
    wget -O - https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz | tar xzv --strip-components 1 && \
    apk del openssl tar && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

EXPOSE 9000
CMD ["/cerebro/bin/cerebro"]
