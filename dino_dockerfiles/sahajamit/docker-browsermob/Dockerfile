
FROM ubuntu:15.04
MAINTAINER Selenium <sahajamit@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get -y install curl zip openjdk-7-jre-headless \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -SL "https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.1.0-beta-3/browsermob-proxy-2.1.0-beta-3-bin.zip" -o "/browsermob-proxy.zip" \
    && unzip -q /browsermob-proxy.zip \
    && rm -f /browsermob-proxy.zip

COPY start.sh /
RUN chmod +x /start.sh

EXPOSE 8080 8019
CMD ["/start.sh"]
