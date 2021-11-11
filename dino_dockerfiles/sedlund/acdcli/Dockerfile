FROM alpine:3.5

MAINTAINER sedlund@github @sredlund

RUN apk add --no-cache git python3 fuse elinks ca-certificates \
    && pip3 install git+https://github.com/yadayada/acd_cli.git \
    && apk del git \
    && addgroup user \
    && adduser -G user -D user

ENV LIBFUSE_PATH=/usr/lib/libfuse.so.2

USER user

ENTRYPOINT ["/usr/bin/acdcli"]

CMD ["-h"]
