FROM alpine:3.4

RUN apk add --no-cache \
    tcpdump \
    bridge-utils \
    netcat-openbsd \
    util-linux \ 
    iperf \
    iptables \
    iputils \
    iproute2 \
    iftop \
    drill \
    apache2-utils \    
    strace \ 
    curl \
    ethtool \
    ngrep


# apparmor issue #14140
RUN mv /usr/sbin/tcpdump /usr/bin/tcpdump

CMD ["sh"]


