FROM alpine
MAINTAINER Martin Baillie <martin.t.baillie@gmail.com>

ENV CONFD_VERSION               0.13.0
ENV CONFD_LOG_LEVEL             debug
ENV CONFD_RANCHER_API_PREFIX    latest
ENV CONFD_RELEASES              https://github.com/kelseyhightower/confd/releases/download

RUN apk add --update --no-cache curl && \
    curl -fSL ${CONFD_RELEASES}/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 \
        -o /bin/confd && \
    chmod +x /bin/confd

ADD run.sh /run.sh
ENTRYPOINT ["/run.sh"]

ONBUILD ADD ./conf.d /etc/confd/conf.d
ONBUILD ADD ./templates /etc/confd/templates
