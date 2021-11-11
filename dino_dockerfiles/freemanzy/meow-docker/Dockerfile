FROM alpine:latest
ENV MEOW_INSTALLDIR=/meow

RUN mkdir /meow && \
    mkdir /lib64 && \
    apk update && \
    apk add --no-cache libc6-compat curl && \
    rm -rf /var/cache/apk/* \
    cp /lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2 && \
    curl -L git.io/meowproxy | sh

WORKDIR /meow
VOLUME /root/.meow
ENTRYPOINT /meow/MEOW
