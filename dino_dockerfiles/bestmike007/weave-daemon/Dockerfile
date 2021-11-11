FROM docker:17.05.0-ce
MAINTAINER Yuanhai He <i@bestmike007.com>

ENV WEAVE_VERSION=1.9.7 \
    DOCKER_VERSION=17.05.0-ce

ADD startup-script.sh /start
RUN apk add --no-cache iptables curl && \
    curl -sSL -o /usr/local/bin/weave https://github.com/weaveworks/weave/releases/download/v${WEAVE_VERSION}/weave && \
    chmod a+x /usr/local/bin/weave /start

ENTRYPOINT ["/start"]
