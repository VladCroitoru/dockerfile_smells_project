FROM alpine:3.4

RUN \
  apk add --update lsyncd && \
  rm -rf /var/cache/apk/*

CMD ["lsyncd", "-nodaemon", "-log", "scarce", "-delay", "0", "-rsync", "/source", "/target"]
