FROM alpine:3.5

RUN apk add -U --no-cache --virtual .fetch-deps \
    ca-certificates \
    openssl \
    tar \
  && wget -O oauth2_proxy.tar.gz https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz \
  && sha256sum oauth2_proxy.tar.gz \
  && echo "1c16698ed0c85aa47aeb80e608f723835d9d1a8b98bd9ae36a514826b3acce56  oauth2_proxy.tar.gz" | sha256sum -c - \
  && tar -zxvf /oauth2_proxy.tar.gz \
  && mv oauth2_proxy*/oauth2_proxy /run/oauth2_proxy \
  && rmdir oauth2_proxy*/ \
  && rm oauth2_proxy.tar.gz \
  && apk del .fetch-deps

EXPOSE 4180

ENTRYPOINT ["/run/oauth2_proxy"]
