FROM phusion/baseimage:0.10.2

# BMP install
ENV BMP_VERSION 2.1.4

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    bzip2 \
    ca-certificates \
    openjdk-8-jre-headless \
    sudo \
    unzip \
    wget \
  	&& rm -rf /var/lib/apt/lists/* \
  	&& sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security \
	&& apt-get clean \
	&& apt-get autoclean \
	&& echo -n > /var/lib/apt/extended_states \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /usr/share/man/?? \
	&& rm -rf /usr/share/man/??_*  \
	&& wget -O browsermob-proxy.zip https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-$BMP_VERSION/browsermob-proxy-$BMP_VERSION-bin.zip \
    && unzip -q /browsermob-proxy.zip \
    && rm -f /browsermob-proxy.zip \
    && mv /browsermob-proxy-$BMP_VERSION /browsermob-proxy



# ENV VALUE
ENV BMP_PORT 8080
ENV PORT_RANGE 8081-8181

COPY rootfs /