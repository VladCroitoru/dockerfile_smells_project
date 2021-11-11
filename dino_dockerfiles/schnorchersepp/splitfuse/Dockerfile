FROM alpine:latest

RUN apk add --no-cache fuse go git musl-dev && \
    sed -i "s/#user_allow_other/user_allow_other/g" /etc/fuse.conf && \
    go get github.com/SchnorcherSepp/splitfuse && \
    go build -o /usr/bin/splitfuse github.com/SchnorcherSepp/splitfuse && \
    go get github.com/ncw/rclone && \
    go build -o /usr/bin/rclone github.com/ncw/rclone && \
    apk del go git musl-dev && \
    rm -R /root/go/ && \
    splitfuse --version && \
    rclone --version

VOLUME ["/config"]

ENTRYPOINT ["/usr/bin/rclone"]

CMD ["--version"]
