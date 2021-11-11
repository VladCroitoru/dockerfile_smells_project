# Configuration-free base from which to build
FROM gliderlabs/alpine:3.4

ARG DOCKER_REPO_VER
ENV DOCKER_REPO_VER=${DOCKER_REPO_VER}

RUN apk update; apk add --upgrade \
        curl \
        tar \
        unzip \
        ca-certificates

# Add Consul
ENV CONSUL_VER=0.6.4
ENV CONSUL_CHECKSUM=abdf0e1856292468e2c9971420d73b805e93888e006c76324ae39416edcf0627
RUN curl --retry 7 -Lso /tmp/consul.zip \
        "https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip" \
  && echo "${CONSUL_CHECKSUM}  /tmp/consul.zip" | sha256sum -c \
  && unzip /tmp/consul -d /usr/local/bin \
  && rm /tmp/consul.zip \
  && mkdir /config
# TODO change /config to /usr/local/etc/consul/config

# Add Consul template
ENV CONSUL_TEMPLATE_VER=0.14.0
ENV CONSUL_TEMPLATE_CHECKSUM=7c70ea5f230a70c809333e75fdcff2f6f1e838f29cfb872e1420a63cdf7f3a78
RUN curl --retry 7 -Lso /tmp/consul-template.zip \
        "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VER}/consul-template_${CONSUL_TEMPLATE_VER}_linux_amd64.zip" \
  && echo "${CONSUL_TEMPLATE_CHECKSUM}  /tmp/consul-template.zip" | sha256sum -c \
  && unzip /tmp/consul-template.zip -d /usr/local/bin \
  && rm /tmp/consul-template.zip

# Add Consul web UI
ENV CONSUL_WEB_CHECKSUM=5f8841b51e0e3e2eb1f1dc66a47310ae42b0448e77df14c83bb49e0e0d5fa4b7
RUN curl --retry 7 -Lso /tmp/consul-webui.zip \
        "https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_web_ui.zip" \
  && echo "${CONSUL_WEB_CHECKSUM}  /tmp/consul-webui.zip" | sha256sum -c \
  && mkdir /ui && unzip /tmp/consul-webui.zip -d /ui \
  && rm /tmp/consul-webui.zip

# Add Containerpilot and set its configuration
ENV CONTAINERPILOT_VER=2.3.0
ENV CONTAINERPILOT_CHECKSUM=0b2dc36172248d0df3b73ad67c3262ed49096e6c1204e2325b3fd7529617f130
# ENV CONTAINERPILOT=file:///etc/containerpilot/containerpilot.json
RUN curl --retry 7 -Lso /tmp/containerpilot.tar.gz \
        "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz" \
  && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/containerpilot.tar.gz" | sha256sum -c \
  && tar xzf /tmp/containerpilot.tar.gz -C /usr/local/bin \
  && rm /tmp/containerpilot.tar.gz

RUN mkdir /usr/local/app /usr/local/etc

# mount Manta next
