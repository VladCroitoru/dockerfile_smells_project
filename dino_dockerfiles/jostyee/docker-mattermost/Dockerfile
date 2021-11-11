FROM frolvlad/alpine-glibc:alpine-3.8
LABEL maintainer="jostyee <git@josta.me>"

ENV MATTERMOST_VERSION=5.4.0 \
    MATTERMOST_HOME="/mattermost"

ENV MATTERMOST_DATA_DIR="${MATTERMOST_HOME}/data"

RUN apk --no-cache add bash gettext \
    mysql-client postgresql-client \
    ca-certificates \
    && apk --no-cache add --virtual .build-deps curl \
    && curl https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz | tar -xz \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/*

EXPOSE 80/tcp

VOLUME ["${MATTERMOST_DATA_DIR}"]
WORKDIR ${MATTERMOST_HOME}

ENTRYPOINT ["bin/mattermost"]
