FROM ubuntu:xenial AS builder

RUN apt-get update && apt-get install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /dehydrated

RUN git clone --depth=1 https://github.com/lukas2511/dehydrated . && mkdir hooks && git clone --depth=1 https://github.com/kappataumu/letsencrypt-cloudflare-hook hooks/cloudflare

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENV GOSU_VERSION 1.10
RUN set -ex; \
	fetchDeps=' \
		ca-certificates \
		wget \
	'; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	rm -rf /var/lib/apt/lists/*; \
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
	gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
	rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \
	chmod +x /usr/local/bin/gosu; \
	gosu nobody true; \ 
	apt-get purge -y --auto-remove $fetchDeps

FROM python:alpine3.6

RUN apk add --update curl libressl bash && \
    rm -rf /var/cache/apk/*

WORKDIR /dehydrated

COPY --from=builder /dehydrated /dehydrated
COPY --from=builder /usr/local/bin /usr/local/bin

RUN pip3 install -r hooks/cloudflare/requirements.txt

COPY config.tmpl config.tmpl
COPY entrypoint.sh /entrypoint.sh

VOLUME /dehydrated/certs
VOLUME /dehydrated/accounts

ENTRYPOINT ["/entrypoint.sh"]
