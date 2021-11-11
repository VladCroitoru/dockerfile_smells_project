# Build
FROM golang:1.9.2 as build

WORKDIR /go/src/github.com/razaj92/aptly-mirror

COPY Makefile .
RUN make setup

COPY . .
RUN make build

# Main
FROM alpine:latest

ENV APTLY_VERSION 1.2.0
ENV GNUPGHOME /var/lib/aptly/gpg

RUN apk --no-cache --progress add git curl bzip2 gnupg1 xz && \
    mkdir -p /app/aptly && \
    curl -L https://bintray.com/artifact/download/smira/aptly/aptly_${APTLY_VERSION}_linux_amd64.tar.gz | tar zx -C /app/aptly --strip-components=1 && \
    ln -s /app/aptly/aptly /usr/bin/aptly && \
    rm -rf /var/cache/apk/*

COPY --from=build /go/src/github.com/razaj92/aptly-mirror/aptly-mirror /usr/local/bin/
COPY files/entrypoint.sh /

RUN addgroup -S -g 501 aptly \
&& adduser -S -s /bin/bash -u 501 -G aptly -h /var/lib/aptly aptly > /dev/null 2>&1

USER 501:501

VOLUME 	/var/lib/aptly

ENTRYPOINT ["aptly-mirror"]
