# Browser Mob Proxy

FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

#========================
# Miscellaneous packages
# Includes minimal runtime used for executing non GUI Java programs
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    bzip2 \
    ca-certificates \
    openjdk-8-jre-headless \
    sudo \
    unzip \
    wget \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security

# BMP install
ENV BMP_VERSION 2.1.4
RUN wget -O browsermob-proxy.zip https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-$BMP_VERSION/browsermob-proxy-$BMP_VERSION-bin.zip \
    && unzip -q /browsermob-proxy.zip \
    && rm -f /browsermob-proxy.zip

RUN mv /browsermob-proxy-$BMP_VERSION /browsermob-proxy

COPY start.sh /
RUN chmod +x /start.sh

# ENV VALUE
ENV BMP_PORT 9090
ENV PORT_RANGE 39500-39999
ENV TTL 600

CMD ["/start.sh"]
