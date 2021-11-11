
FROM alpine:3.11 as builder

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG QUASSELWEB_VERSION

ENV \
  TERM=xterm \
  QUASSEL_HOST=localhost \
  QUASSEL_PORT=4242 \
  FORCE_DEFAULT=true \
  WEBSERVER_MODE=http \
  WEBSERVER_PORT=64080

# ---------------------------------------------------------------------------------------

RUN \
  echo "export BUILD_DATE=${BUILD_DATE}"              > /etc/profile.d/quassel-web.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}"             >> /etc/profile.d/quassel-web.sh

# hadolint ignore=DL3017,DL3018,DL3019
RUN \
  apk update  --quiet && \
  apk upgrade --quiet

# hadolint ignore=DL3018,DL3019
RUN \
  apk add     --quiet \
    build-base \
    curl \
    git \
    nodejs-npm \
    nodejs \
    openssl \
    python

WORKDIR /data

RUN \
  git clone https://github.com/magne4000/quassel-webserver.git

WORKDIR /data/quassel-webserver

# hadolint ignore=SC2039,DL4006
RUN \
  if [ "${BUILD_TYPE}" = "stable" ] ; then \
    echo "switch to stable Tag v${QUASSELWEB_VERSION}" && \
    git checkout tags/${QUASSELWEB_VERSION} 2> /dev/null && \
    echo "export QUASSELWEB_VERSION=${QUASSELWEB_VERSION}" >> /etc/profile.d/quassel-web.sh ; \
  else \
    version=$(git describe --tags --always | sed 's/^v//') && \
    echo -e "\n use BUILD_TYPE: '${BUILD_TYPE}'" && \
    echo -e " build version: ${version}\n" && \
    echo "export QUASSELWEB_VERSION=${version}" >> /etc/profile.d/quassel-web.sh ; \
  fi

# hadolint ignore=DL3016
RUN \
  npm i -g npm && \
  npm i --package-lock-only && \
  # npm install acorn && \
  npm install --production

# hadolint ignore=DL4006
RUN \
  npm ls -gp --depth=0 | awk -F/node_modules/ '{print $2}' | grep -vE '^(npm|)$' | xargs -r npm -g rm && \
  rm -rf \
    /data/quassel-webserver/.git* && \
  find \
    . -type f -iname "*.md" -delete && \
  find \
    . -type f -iname "Makefile" -delete && \
  find \
    . -type f -iname ".travis.yml" -delete && \
  find \
    . -type f -iname ".npmignore" -delete && \
  find \
    . -type f -iname ".jshintrc" -delete && \
  find \
    . -type f -iname "yarn.lock" -delete && \
  find \
    . -type f -iname "*CONTRIBUTING*" -delete

# ---------------------------------------------------------------------------------------

FROM alpine:3.11

ENV \
  TZ='Europe/Berlin'

COPY --from=builder /etc/profile.d/quassel-web.sh /etc/profile.d/quassel-web.sh
COPY --from=builder /data/quassel-webserver       /data/quassel-webserver

# hadolint ignore=SC1091,DL3017,DL3018,DL4006
RUN \
  . /etc/profile && \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache --virtual .build-deps \
    shadow \
    tzdata && \
  apk add --no-cache \
    curl \
    ca-certificates \
    nodejs \
    openssl && \
  cp "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/localtime && \
  /usr/sbin/useradd \
    --user-group \
    --shell /bin/false \
    --comment "User for quassel web" \
    --no-create-home \
    --home-dir /data/quassel-webserver \
    --uid 1000 \
    quassel && \
  chown -R quassel:quassel /data/quassel-webserver && \
  apk del --quiet --purge .build-deps && \
  rm -rf \
    /tmp/* \
    /root/.n* \
    /var/cache/apk/*

COPY rootfs/ /

USER quassel
WORKDIR /data/quassel-webserver

VOLUME ["/data/quassel-webserver/ssl"]

CMD ["/init/run.sh"]

# ---------------------------------------------------------------------------------------

EXPOSE 64080 64443

HEALTHCHECK \
  --interval=10s \
  --timeout=10s \
  --retries=12 \
  --start-period=10s \
  CMD /init/health_check.sh

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Quassel Webserver Docker Image" \
  org.label-schema.description="Inofficial Quassel Webserver Docker Image" \
  org.label-schema.url="https://github.com/magne4000/quassel-webserver" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-quassel-web" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${QUASSELWEB_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"

# ---------------------------------------------------------------------------------------
