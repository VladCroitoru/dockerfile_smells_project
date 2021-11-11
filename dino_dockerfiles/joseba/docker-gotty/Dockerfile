FROM alpine:3.4

EXPOSE 8080

RUN apk add --update go bash openssh-client git && \
  mkdir -p /tmp/gotty && \
  GOPATH=/tmp/gotty go get github.com/yudai/gotty && \
  mv /tmp/gotty/bin/gotty /usr/local/bin/ && \
  apk del go git && \
  rm -rf /tmp/gotty /var/cache/apk/*

VOLUME ["/config"]

ENTRYPOINT ["/usr/local/bin/gotty"]

CMD ["--config","/config/gotty.conf","--permit-write","--reconnect","/bin/bash"]
