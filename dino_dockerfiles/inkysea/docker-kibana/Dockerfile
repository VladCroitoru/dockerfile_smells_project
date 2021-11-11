FROM alpine:3.6

ENV KIBANA_VERSION 5.5.1-linux-x86_64

RUN apk --update add curl && \
    mkdir /opt && \
    curl -s https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}.tar.gz | tar zx -C /opt && \
    apk add nodejs && \
    rm -rf /opt/kibana-${KIBANA_VERSION}/node && \
    mkdir -p /opt/kibana-${KIBANA_VERSION}/node/bin && \
    ln -sf /usr/bin/node /opt/kibana-${KIBANA_VERSION}/node/bin/node && \
    apk del curl && \
    rm -rf /var/cache/apk/*

ADD ./run.sh /run.sh

EXPOSE 5601

ENTRYPOINT /run.sh
