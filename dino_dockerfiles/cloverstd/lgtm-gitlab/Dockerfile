FROM alpine:3.5
MAINTAINER cloverstd https://github.com/cloverstd

ENV LGTM_VERSION=0.1.0
ENV LGTM_BINARY_URL=https://github.com/cloverstd/lgtm-gitlab/releases/download/v$LGTM_VERSION/lgtm-alpine-linux-amd64-v$LGTM_VERSION.tar.gz

RUN apk add --no-cache --virtual .build_deps curl && \
    cd /tmp && \
    curl -slL $LGTM_BINARY_URL -o /tmp/lgtm.tar.gz && \
    tar zxvf lgtm.tar.gz && \
    chmod +x lgtm && \
    mv lgtm / && \
    apk del .build_deps && \
    mkdir /var/lib/lgtm && \
    rm -rf /var/cache/* && \
    rm -rf /tmp/*

ENV LGTM_NOTE=LGTM \
    LGTM_COUNT=2 \
    LGTM_PORT=8989 \
    LGTM_TOKEN= \
    LGTM_GITLAB_URL=http://gitlab.com \
    LGTM_DB_PATH=/var/lib/lgtm/lgtm.data \
    LGTM_LOG_LEVEL=info

VOLUME /var/lib/lgtm
EXPOSE 8989

CMD ["sh", "-c",\
    "/lgtm -token $LGTM_TOKEN -gitlab_url $LGTM_GITLAB_URL -lgtm_count $LGTM_COUNT -lgtm_note $LGTM_NOTE -log_level $LGTM_LOG_LEVEL -db_path $LGTM_DB_PATH -port $LGTM_PORT"\
]

