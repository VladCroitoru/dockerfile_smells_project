FROM gliderlabs/alpine:3.3

MAINTAINER "Daniel Whatmuff" <danielwhatmuff@gmail.com>

ENV GLIBC_VERSION 2.22-r8

RUN apk-install curl ca-certificates && \
    curl -O -L https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk -o glibc-${GLIBC_VERSION}.apk && \
    apk --allow-untrusted add glibc-${GLIBC_VERSION}.apk && \
    rm -f glibc-${GLIBC_VERSION}.apk && \
    rm -rf /root/.cache && \
    rm -rf /var/cache/apk/ && \
    apk version glibc && \
    ls /lib64/

CMD ["echo", "Alpine + glibc base image"]
