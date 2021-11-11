FROM alpine:3.6

RUN set -ex && \
    echo "http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    apk update && \
    apk add --no-cache \
      apache2-utils \
      bridge-utils \
      conntrack-tools \
      curl \
      drill \
      ethtool \
      iftop \
      iperf \
      iproute2 \
      iptables \
      iputils \
      ipvsadm \
      jq \
      netcat-openbsd \
      ngrep \
      nmap \
      socat \
      strace \
      tcpdump \
      util-linux

# apparmor issue #14140
RUN mv /usr/sbin/tcpdump /usr/bin/tcpdump

COPY netgen.sh /usr/local/bin/netgen

CMD ["sh"]
