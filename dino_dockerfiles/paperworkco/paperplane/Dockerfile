FROM alpine:latest

RUN apk update \
 && apk add curl unzip bash jq ca-certificates \
 && rm -rf /var/cache/apk/*

# Install Consul
# Releases at https://releases.hashicorp.com/consul
RUN set -ex \
    && export CONSUL_VERSION=1.0.6 \
    && export CONSUL_CHECKSUM=bcc504f658cef2944d1cd703eda90045e084a15752d23c038400cf98c716ea01 \
    && curl --retry 7 --fail -vo /tmp/consul.zip "https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip" \
    && echo "${CONSUL_CHECKSUM}  /tmp/consul.zip" | sha256sum -c \
    && unzip /tmp/consul -d /usr/local/bin \
    && rm /tmp/consul.zip \
    # Create empty directories for Consul config and data \
    && mkdir -p /etc/consul \
    && mkdir -p /var/lib/consul \
    && mkdir /config

# Install Consul template
# Releases at https://releases.hashicorp.com/consul-template/
RUN set -ex \
    && export CONSUL_TEMPLATE_VERSION=0.19.4 \
    && export CONSUL_TEMPLATE_CHECKSUM=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0 \
    && curl --retry 7 --fail -Lso /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \
    && echo "${CONSUL_TEMPLATE_CHECKSUM}  /tmp/consul-template.zip" | sha256sum -c \
    && unzip /tmp/consul-template.zip -d /usr/local/bin \
    && rm /tmp/consul-template.zip

# Add Containerpilot and set its configuration
ENV CONTAINERPILOT /etc/containerpilot.json5
ENV CONTAINERPILOT_VERSION 3.7.0

RUN export CONTAINERPILOT_CHECKSUM=b10b30851de1ae1c095d5f253d12ce8fe8e7be17 \
    && export archive=containerpilot-${CONTAINERPILOT_VERSION}.tar.gz \
    && curl -Lso /tmp/${archive} \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/${archive}" \
    && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/${archive}" | sha1sum -c \
    && tar zxf /tmp/${archive} -C /usr/local/bin \
    && rm /tmp/${archive}

COPY /*.sh /usr/local/bin/
RUN chmod 500 /usr/local/bin/*.sh

ENTRYPOINT []
CMD ["containerpilot"]
