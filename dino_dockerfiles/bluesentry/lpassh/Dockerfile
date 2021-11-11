FROM alpine:latest
LABEL maintainer="dennis@bluesentryit.com"
LABEL Description="Reads ssh keys and settings from LastPass Secure Notes"

WORKDIR /usr/local/src

RUN apk add --no-cache --update ca-certificates curl-dev libxml2-dev git gcc g++ automake make cmake bash openssh-client && \
    git clone https://github.com/LastPass/lastpass-cli.git && \
    cd /usr/local/src/lastpass-cli && make && make install && make clean && \
    apk del git gcc g++ automake make cmake && \
    rm -rf /var/cache/apk/*

ADD lpassh /usr/local/bin/

ENTRYPOINT ["lpassh"]