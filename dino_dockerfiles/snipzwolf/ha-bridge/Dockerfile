FROM ubuntu:bionic

ENV SERVERPORT="80" \
    VERSION="5.3.0" \
    DEBCONF_NONINTERACTIVE_SEEN="true" \
    DEBIAN_FRONTEND="noninteractive"

WORKDIR /

RUN apt-get update && \
    apt-get -y install wget libcap2-bin netcat openjdk-8-jre-headless && \
    usermod -u 99 nobody && \
    usermod -g 100 nobody && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /ha-bridge-scripts
ADD src/* ./

WORKDIR /config
RUN wget -q -O ./ha-bridge.jar https://github.com/bwssytems/ha-bridge/releases/download/v"$VERSION"/ha-bridge-"$VERSION".jar && \
    mkdir /config/startup-config/

RUN whereis -b java && \
    setcap 'cap_net_bind_service=+ep' $(readlink -f `which java`)

RUN chmod -R 0775 /ha-bridge-scripts && \
    chmod -R 0776 /config && \
    chown -R nobody:users /config

VOLUME ["/config/data"]
ENTRYPOINT /ha-bridge-scripts/new_entrypoint
