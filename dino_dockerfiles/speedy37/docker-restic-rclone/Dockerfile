FROM alpine:3.7

RUN apk add --no-cache git go musl-dev ca-certificates fuse \
 && mkdir -p /root/go/src/github.com/ncw \
 && cd /root/go/src/github.com/ncw \
 && git clone https://github.com/Speedy37/rclone.git \
 && cd rclone \
 && go build \
 && mv rclone /usr/local/bin/rclone \
 && cd /root \
 && git clone https://github.com/Speedy37/restic.git \
 && cd restic && git checkout rclone \
 && go run build.go \
 && mv restic /usr/local/bin/restic \
 && cd /root \
 && rm -r /root/go restic \
 && apk del git go musl-dev \
 && echo "DONE"

VOLUME ["/root/.config/rclone/", "/root/.cache/restic/"]
