FROM alpine:3.3

ENV CONSUL_TEMPLATE_VERSION=0.14.0

RUN apk add --update curl && \
    curl -LO http://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    apk del openssl ca-certificates curl libssh2 && \
    rm -rf /var/lib/apt/lists/* && \
    unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mv consul-template /usr/local/bin/consul-template && \
    rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mkdir -p /consul-template

VOLUME /consul-template

ENTRYPOINT ["/usr/local/bin/consul-template"]
