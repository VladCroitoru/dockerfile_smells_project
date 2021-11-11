FROM docker:17.09

ARG DOCKER_MACHINE_VERSION=0.13.0
ARG DOCKER_COMPOSE_VERSION=1.19.0

RUN set -x && \
    apk add --no-cache -t .deps ca-certificates curl && \
    # Install glibc on Alpine (required by docker-compose) from
    # https://github.com/sgerrand/alpine-pkg-glibc
    # See also https://github.com/gliderlabs/docker-alpine/issues/11
    GLIBC_VERSION='2.23-r3' && \
    curl -Lo /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    curl -Lo glibc.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk && \
    curl -Lo glibc-bin.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk && \
    apk update && \
    apk add glibc.apk glibc-bin.apk && \
    rm -rf /var/cache/apk/* && \
    rm glibc.apk glibc-bin.apk && \
    \
    # Clean-up
    apk del .deps

RUN set -ex; \
	apk add --no-cache --virtual .fetch-deps \
		curl \
	; \
	\
	if ! curl -L https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-machine-`uname -s`-`uname -m` -o /tmp/docker-machine; then \
		echo >&2 "error: failed to download 'docker-machine-${DOCKER_MACHINE_VERSION}'"; \
		exit 1; \
	fi; \
	\
	chmod +x /tmp/docker-machine; \
    cp /tmp/docker-machine /usr/local/bin/docker-machine; \
	\
	if ! curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` -o /tmp/docker-compose; then \
		echo >&2 "error: failed to download 'docker-compose-${DOCKER_COMPOSE_VERSION}'"; \
		exit 1; \
	fi; \
	\
	chmod +x /tmp/docker-compose; \
    cp /tmp/docker-compose /usr/local/bin/docker-compose; \
	\
	apk del .fetch-deps;