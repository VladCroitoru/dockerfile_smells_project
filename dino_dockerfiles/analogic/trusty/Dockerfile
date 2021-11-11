FROM ubuntu-debootstrap:trusty
MAINTAINER info@analogic.cz

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]

RUN echo "Europe/Prague" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata && update-locale
