FROM debian:jessie-slim
MAINTAINER Ryan Eschinger <ryanesc@gmail.com>

ENV HUGO_VERSION=0.18.1

RUN apt-get -qq update && \
  DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-recommends \
  wget \
  python-pygments \
  ca-certificates && \
  cd /tmp/ && \
  wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  rm -r hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  mv hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64 /usr/bin/hugo && \
  rm -rf hugo_${HUGO_VERSION}_linux_amd64 \
  && rm -rf /var/lib/apt/lists/*

VOLUME /src
WORKDIR /src

CMD ["/usr/bin/hugo"]
