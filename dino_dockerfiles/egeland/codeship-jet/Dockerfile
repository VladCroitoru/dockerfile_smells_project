FROM alpine:latest

ENV JET_VERSION 1.18.15

RUN apk --no-cache add --virtual .build-deps curl tar && \
    curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/${JET_VERSION}/jet-linux_amd64_${JET_VERSION}.tar.gz" && \
    tar -xaC /usr/local/bin -f jet-linux_amd64_${JET_VERSION}.tar.gz && \
    chmod +x /usr/local/bin/jet && \
    apk del .build-deps && \
    rm -f jet-linux_amd64_${JET_VERSION}.tar.gz

WORKDIR /root

ENTRYPOINT ["/usr/local/bin/jet"]

