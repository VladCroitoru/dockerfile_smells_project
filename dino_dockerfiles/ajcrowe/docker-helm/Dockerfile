FROM alpine:3

ENV VERSION v3.2.4

RUN apk add --no-cache --virtual build-dependencies curl && \
    mkdir -p /tmp/helm && \
    curl https://get.helm.sh/helm-${VERSION}-linux-amd64.tar.gz | \
      tar -xzv -C /tmp/helm && \
    mv /tmp/helm/linux-amd64/helm /usr/bin/helm && \
    rm -rf /tmp/helm && \
    apk del build-dependencies

RUN apk add git gettext ca-certificates

CMD ["/usr/bin/helm"]
