FROM alpine:3.13
# hadolint ignore=DL3018
RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    echo '@community http://dl-cdn.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories && \
    apk add --update --no-cache \
        bash \
        dma@testing \
        gosu@testing \
        iproute2 \
        knot-resolver@community \
        knot-utils \
        mailx \
        mtr \
    && \
    ln -s /usr/bin/kdig /usr/local/bin/dig && \
    ln -s /usr/bin/khost /usr/local/bin/host
COPY entrypoint /usr/local/sbin/entrypoint
WORKDIR /
ENTRYPOINT [ "entrypoint" ]
CMD [ "bash", "--login" ]
