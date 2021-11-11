FROM alpine:3.13

RUN apk add --update curl openssl bind-tools docker bash nmap netcat-openbsd tcpdump iotop sysstat iftop socat && \
  rm -rf /var/cache/apk/*

ENTRYPOINT ["bash"]
