FROM resin/armv7hf-debian-qemu

RUN [ "cross-build-start" ]

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'deb http://deb.torproject.org/torproject.org jessie main' > /etc/apt/sources.list.d/tor.list && \
    gpg --keyserver keys.gnupg.net --recv 886DDD89 && \
    gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -
RUN apt-get update && apt-get install -y \
    deb.torproject.org-keyring \
    obfsproxy \
    openssl \
    tor

WORKDIR /var/lib/tor
VOLUME /var/lib/tor

ADD run.sh /var/lib/tor
ENTRYPOINT "/var/lib/tor/run.sh"

RUN [ "cross-build-end" ]  
