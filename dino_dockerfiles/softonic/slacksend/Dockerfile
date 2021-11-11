FROM alpine:latest

RUN apk add --update curl bash jq && \
    rm -rf /var/cache/apk/*

ADD ./slacksend /usr/local/bin/slacksend

ENTRYPOINT ["/usr/local/bin/slacksend"]
