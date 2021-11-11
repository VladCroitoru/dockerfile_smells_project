FROM ubuntu:14.04
MAINTAINER Bryan Kendall <bryan@runnable.com>

EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600/udp

ENV CONSUL_VERSION 0.6.4
ENV CONSUL_ZIP /tmp/consul.zip
ENV CONSUL_UI_ZIP /tmp/ui.zip

RUN apt-get update && \
    apt-get install -y wget zip && \
    wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip -q -O ${CONSUL_ZIP} && \
    unzip ${CONSUL_ZIP} -d /usr/local/bin && \
    rm ${CONSUL_ZIP} && \
    wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip -q -O ${CONSUL_UI_ZIP} && \
    mkdir /ui && \
    unzip ${CONSUL_UI_ZIP} -d /ui && \
    rm ${CONSUL_UI_ZIP}

CMD ["/usr/local/bin/consul"]
