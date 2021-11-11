FROM debian:buster-slim
MAINTAINER foo@example.com
RUN export DEBIAN_FRONTEND='noninteractive' && \
    apt-get update -qq && \
    apt-get install -qqy --no-install-recommends openvpn \
                $(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}') &&\
                apt-get clean && \
                rm -rf /var/lib/apt/lists/* /tmp/*

VOLUME ["/vpn"]
ENTRYPOINT ["openvpn"]
