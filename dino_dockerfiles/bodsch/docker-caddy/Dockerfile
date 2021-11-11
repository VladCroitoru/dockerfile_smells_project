
FROM alpine:3.6

MAINTAINER Bodo Schulz <bodo@boone-schulz.de>

ENV \
  ALPINE_MIRROR="mirror1.hs-esslingen.de/pub/Mirrors" \
  ALPINE_VERSION="v3.6" \
  GOPATH=/opt/go \
  GOROOT=/usr/lib/go \
  GOMAXPROCS=4 \
  TERM=xterm \
  BUILD_DATE="2017-10-25" \
  BUILD_TYPE="stable" \
  VERSION="0.10.10" \
  PLUGINS="authz login minify realip forwardproxy"

EXPOSE 80 443 2015

LABEL \
  version="1710" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Caddy Docker Image" \
  org.label-schema.description="Inofficial Caddy Docker Image" \
  org.label-schema.url="https://caddyserver.com" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-caddy" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${ICINGA_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="MIT License"

# ---------------------------------------------------------------------------------------
# install caddy
# COPY --from=builder /install/caddy /usr/bin/caddy

RUN \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main"       > /etc/apk/repositories && \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >> /etc/apk/repositories && \
  apk --quiet --no-cache update && \
  apk --quiet --no-cache upgrade && \
  apk --no-cache add --virtual .build-deps \
    g++ git go make && \
  echo "get sources ..." && \
  go get github.com/mholt/caddy || true && \
  cd ${GOPATH}/src/github.com/mholt/caddy && \
  #
  # switch to tag
  if [ "${BUILD_TYPE}" == "stable" ] ; then \
    echo "switch to stable Tag v${VERSION}" && \
    git checkout tags/v${VERSION} 2> /dev/null ; \
  fi && \
  # plugin helper
  go get -v github.com/abiosoft/caddyplug/caddyplug && \
  GOOS=linux \
  GOARCH=amd64 \
  PATH=${GOPATH}/bin/:$PATH && \
  alias caddyplug='GOOS=linux GOARCH=amd64 caddyplug' && \
  # plugins
  for plugin in $(echo $PLUGINS | tr "," " "); do \
    echo "get plugin ${plugin}" ; \
    go get -v $(caddyplug package $plugin) || true; \
    printf "package caddyhttp\nimport _ \"$(caddyplug package $plugin)\"" > ${GOPATH}/src/github.com/mholt/caddy/caddyhttp/$plugin.go ; \
  done && \
  git clone https://github.com/caddyserver/builds ${GOPATH}/src/github.com/caddyserver/builds && \
  # build
  cd ${GOPATH}/src/github.com/mholt/caddy/caddy && \
    git checkout -f && \
    GOOS=linux GOARCH=amd64 go run build.go -goos=$GOOS -goarch=$GOARCH -goarm=$GOARM && \
    mv caddy /usr/bin && \
  # validate install
  /usr/bin/caddy -version && \
  /usr/bin/caddy -plugins && \
  # clean up
  go clean -i -r && \
  apk del .build-deps && \
  rm -rf \
    ${GOPATH} \
    /usr/lib/go \
    /usr/bin/go* \
    /tmp/* \
    /var/cache/apk/* \
    /root/.cache \
    /root/.config \
    /root/lib \
    /usr/local/*

COPY rootfs/ /

VOLUME [ "/root/.caddy" "/srv" ]
WORKDIR /srv

ENTRYPOINT [ "/usr/bin/caddy" ]
CMD [ "--conf", "/etc/Caddyfile", "--log", "stdout" ]
