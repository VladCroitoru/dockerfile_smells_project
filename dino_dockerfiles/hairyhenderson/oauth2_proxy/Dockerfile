FROM alpine:3.11 AS download

RUN apk --no-cache add curl ca-certificates
RUN curl -sSL https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz \
  | tar zxv --strip-components=1 -C /
RUN chmod 755 /oauth2_proxy

FROM debian:9.8 AS compress

RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -yq curl xz-utils ca-certificates
RUN curl -fsSL -o /tmp/upx.tar.xz https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz \
  && tar Jxv -C /tmp --strip-components=1 -f /tmp/upx.tar.xz

COPY --from=download /oauth2_proxy /
RUN /tmp/upx --lzma /oauth2_proxy -o /oauth2_proxy-slim

FROM alpine:3.11

COPY --from=download /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt 
COPY --from=compress /oauth2_proxy-slim /bin/oauth2_proxy

ENTRYPOINT [ "oauth2_proxy" ]
CMD ["--help"]
