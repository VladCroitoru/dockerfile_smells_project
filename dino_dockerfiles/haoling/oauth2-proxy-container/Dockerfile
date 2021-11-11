FROM buildpack-deps:jessie-curl

ENV OAUTH2_PROXY_VERSION=2.0.1
ENV GOLANG_VERSION=1.4.2
ENV ARCHIVE=oauth2_proxy-$OAUTH2_PROXY_VERSION.linux-amd64.go$GOLANG_VERSION
ENV PATH /opt/oauth2-proxy/bin:$PATH

RUN mkdir -p /opt/oauth2-proxy/bin && mkdir /opt/oauth2-proxy/etc && \
    curl -L -k --silent \
      https://github.com/bitly/oauth2_proxy/releases/download/v$OAUTH2_PROXY_VERSION/$ARCHIVE.tar.gz  | \
      tar xz --strip-components 1 -C /opt/oauth2-proxy/bin

CMD oauth2_proxy -config=/opt/oauth2-proxy/etc/config

