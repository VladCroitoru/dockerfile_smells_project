
FROM alpine:3.6

MAINTAINER Bodo Schulz <bodo@boone-schulz.de>

ENV \
  ALPINE_MIRROR="mirror1.hs-esslingen.de/pub/Mirrors" \
  ALPINE_VERSION="v3.6" \
  WEBPROC_VERSION=0.1.7 \
  TERM=xterm \
  BUILD_DATE="2017-06-15" \
  APK_ADD="ca-certificates curl dnsmasq" \
  APK_DEL="curl"

EXPOSE 5353 5353/udp 8000

LABEL \
  version="1706-02.1" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile"

# ---------------------------------------------------------------------------------------

RUN \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main"       > /etc/apk/repositories && \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >> /etc/apk/repositories && \
  apk update  --quiet --no-cache  && \
  apk upgrade --quiet --no-cache  && \
  for apk in ${APK_ADD} ; \
  do \
    apk add --quiet --no-cache ${apk} ; \
  done && \
  curl \
    --silent \
    --location \
    --retry 3 \
    --retry-delay 10 \
    --retry-connrefused \
    https://github.com/jpillora/webproc/releases/download/${WEBPROC_VERSION}/webproc_linux_amd64.gz | \
      gzip -d - > /usr/bin/webproc && \
  chmod +x /usr/bin/webproc && \
  mkdir -p /etc/default/ && \
  echo -e "ENABLED=1\nIGNORE_RESOLVCONF=yes" > /etc/default/dnsmasq  && \
  for apk in ${APK_DEL} ; \
  do \
    apk --quiet --purge del ${apk} ; \
  done && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

COPY rootfs/ /

CMD [ "/init/run.sh" ]

# COPY dnsmasq.conf /etc/dnsmasq.conf
# CMD ["webproc","--config","/etc/dnsmasq.conf", "--port", "8000", "--", "dnsmasq", "--no-daemon"]
