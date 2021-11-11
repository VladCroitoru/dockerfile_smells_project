FROM ubuntu:latest

MAINTAINER Beshoy Girgis <shoy@1ds.us>

ENV DEBIAN_FRONTEND="noninteractive"

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ADD ./services.d /etc/services.d
ADD ./cont-init.d /etc/cont-init.d
RUN chmod -R +x /etc/services.d/*/run

RUN apt-get update \
    && apt-get -y install \
        curl \
        git \
        sudo \
        unzip \
        vim

# RUN git clone https://github.com/nylas/sync-engine.git \
#     && rm -rf /opt/sync-engine/.git
WORKDIR /opt
ENV TAG=91e3a8bff6ef0656eca9e356c07963c8b238d876
RUN curl -L -O https://github.com/nylas/sync-engine/archive/${TAG}.zip \
    && unzip ${TAG}.zip \
    && rm ${TAG}.zip \
    && mv sync-engine-${TAG} sync-engine

WORKDIR /opt/sync-engine

RUN groupadd -g 1000 inbox \
    && useradd -u 1000 -g inbox -s /bin/bash inbox

ADD setup.sh /opt/sync-engine/setup.sh

RUN export SUDO_UID=1000 \
    && export SUDO_GID=1000 \
    && ./setup.sh -p true

RUN sed -i 's/localhost/mysql/' /etc/inboxapp/secrets.yml \
    && head -n -3 /etc/inboxapp/secrets.yml > /etc/inboxapp/secrets2.yml \
    # Remove second part of first shard
    && sed -i '11,15d' /etc/inboxapp/config.json \
    # Remove second shard
    && sed -i '13,29d' /etc/inboxapp/config.json \
    && sed -i 's/localhost/mysql/' /etc/inboxapp/config.json \
    && sed -i 's/127.0.0.1/mysql/' /etc/inboxapp/config.json \
    && sed -i 's/\["mysql"\]/["redis"]/g' /etc/inboxapp/config.json \
    && sed -i 's/"ACCOUNT_QUEUE_REDIS_HOSTNAME": "mysql",/"ACCOUNT_QUEUE_REDIS_HOSTNAME": "redis",/g' /etc/inboxapp/config.json \
    && sed -i 's/"UMPIRE_BASE_URL": "mysql",/"UMPIRE_BASE_URL": "127.0.0.1",/g' /etc/inboxapp/config.json

RUN apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/*

ADD my.local.cnf /etc/my.local.cnf

EXPOSE 5555

VOLUME ["/run", "/var/lib/inboxapp/parts/"]
ENTRYPOINT ["/init"]
