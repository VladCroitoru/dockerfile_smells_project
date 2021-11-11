FROM alpine:3.4

RUN echo http://nl.alpinelinux.org/alpine/v3.4/community >> /etc/apk/repositories \
  && apk add --no-cache ca-certificates curl fuse jq git go python3 \
  && pip3 install acdcli \
  && mkdir ~/.cache/acd_cli \
  && mkdir /mounted \
  && git clone https://github.com/restic/restic \
  && cd restic \
  && go run build.go \
  && cp restic /usr/local/bin/ \
  && apk del git go

ENV LIBFUSE_PATH=/usr/lib/libfuse.so.2
ENV RESTIC_REPOSITORY=/mounted/Backups

VOLUME /data

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["restic", "backup", "/data"]
