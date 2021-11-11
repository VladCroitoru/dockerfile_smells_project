FROM alpine
MAINTAINER Koichi Nakashima <koichi@nksm.name>

RUN apk add --update bash coreutils wget ca-certificates bind-tools jq \
    && rm -rf /var/cache/apk/*

RUN wget -q https://github.com/ko1nksm/docker-client-only-binary/raw/master/docker-1.10.2-upx -O /usr/local/bin/docker \
    && chmod +x /usr/local/bin/docker

COPY docker-events-plugin /
COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["exec"]
