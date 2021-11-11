FROM haproxy
MAINTAINER Volodymyr Kuznetsov <ks.vladimir@gmail.com>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl iptables && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
