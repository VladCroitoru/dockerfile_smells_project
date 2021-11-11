FROM traefik:1.7-alpine

MAINTAINER Jesse DeFer <traefik-vault@dotd.com>

ENV DOCKER_BASE_VERSION=0.0.4
ENV CONSUL_TEMPLATE_VERSION=0.19.5

ENV HASHICORP_RELEASES=https://releases.hashicorp.com

RUN apk add --no-cache ca-certificates gnupg openssl && \
    gpg --keyserver pool.sks-keyservers.net --recv-keys 91A6E7F85D05C65630BEF18951852D87348FFC4C && \
    mkdir -p /tmp/build && \
    cd /tmp/build && \
    wget ${HASHICORP_RELEASES}/docker-base/${DOCKER_BASE_VERSION}/docker-base_${DOCKER_BASE_VERSION}_linux_amd64.zip && \
    wget ${HASHICORP_RELEASES}/docker-base/${DOCKER_BASE_VERSION}/docker-base_${DOCKER_BASE_VERSION}_SHA256SUMS && \
    wget ${HASHICORP_RELEASES}/docker-base/${DOCKER_BASE_VERSION}/docker-base_${DOCKER_BASE_VERSION}_SHA256SUMS.sig && \
    gpg --batch --verify docker-base_${DOCKER_BASE_VERSION}_SHA256SUMS.sig docker-base_${DOCKER_BASE_VERSION}_SHA256SUMS && \
    grep ${DOCKER_BASE_VERSION}_linux_amd64.zip docker-base_${DOCKER_BASE_VERSION}_SHA256SUMS | sha256sum -c && \
    unzip docker-base_${DOCKER_BASE_VERSION}_linux_amd64.zip && \
    cp bin/gosu bin/dumb-init /bin && \
    wget ${HASHICORP_RELEASES}/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    wget ${HASHICORP_RELEASES}/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS && \
    wget ${HASHICORP_RELEASES}/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS.sig && \
    gpg --batch --verify consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS.sig consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS && \
    grep consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS | sha256sum -c && \
    unzip -d /bin consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    cd /tmp && \
    rm -rf /tmp/build && \
    apk del gnupg openssl && \
    rm -rf /root/.gnupg

# The agent will be started with /consul-template/config as the configuration directory
# so you can add additional config files in that location.
RUN mkdir -p /consul-template/config /consul-template/templates

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["traefik"]
