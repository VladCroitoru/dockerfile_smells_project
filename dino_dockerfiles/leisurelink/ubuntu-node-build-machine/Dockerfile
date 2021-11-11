FROM ubuntu:14.04
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>

ENV NODE_VERSION 4.2.4

COPY rootfs /

ADD https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz /tmp/node-v${NODE_VERSION}-linux-x64.tar.gz

RUN set -ex && \
  cd /tmp && \
  tar -xzf /tmp/node-v${NODE_VERSION}-linux-x64.tar.gz -C /usr/local --strip-components=1 && \
  apt-get update && \
  apt-get install -y openssl git libssl-dev libkrb5-dev python-dev linux-headers-4.2.0-22-generic build-essential && \
  ssh-keyscan -t rsa github.com >> /etc/ssh/ssh_known_hosts && \
  chmod +x /opt/lib/perform-build.sh && \
  ln -s /opt/lib/perform-build.sh /usr/local/bin/perform-build && \
  groupadd node && \
  useradd -m -g node node && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* \
         /var/tmp/* \
         /tmp/*

VOLUME ["/source"]

USER node
WORKDIR /source
CMD ["perform-build"]