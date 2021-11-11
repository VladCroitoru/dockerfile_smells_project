FROM golang:alpine AS go

RUN set -x && \
  apk add --update git && \
  go get -u -v github.com/rakyll/hey && \
  go get -u -v github.com/astaxie/bat

FROM alpine
COPY --from=go /go/bin/hey /usr/local/bin/hey
COPY --from=go /go/bin/bat /usr/local/bin/bat

RUN set -ex \
    && echo "http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache \
    tcpdump \
    bridge-utils \
    netcat-openbsd \
    util-linux \
    iptables \
    iputils \
    iproute2 \
    iftop \
    drill \
    apache2-utils \
    strace \
    curl \
    ethtool \
    ipvsadm \
    ngrep \
    iperf \
    nmap \
    conntrack-tools \
    bash \
    jq \
    vim \
    git \
    tree \
    the_silver_searcher

RUN set -ex \
  && curl -L -o /usr/local/bin/filla https://releases.filla.be/linux-amd64/filla \
  && chmod +x /usr/local/bin/filla

RUN mv /usr/sbin/tcpdump /usr/bin/tcpdump

ADD netgen.sh /usr/local/bin/netgen
ENTRYPOINT [ "/bin/bash" ]
