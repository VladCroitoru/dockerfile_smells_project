FROM alpine:3.11

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG GRAPHITE_VERSION

ENV \
  TZ='Europe/Berlin' \
  TERM=xterm

# 2003: Carbon line receiver port
# 7002: Carbon cache query port
# 8080: Graphite-Web port
EXPOSE 2003 2003/udp 7002 8080

# ---------------------------------------------------------------------------------------

WORKDIR /tmp
# hadolint ignore=DL3003,DL3013,DL3017,DL3018,DL3019,SC2015
RUN \
  echo "export BUILD_DATE=${BUILD_DATE}"              > /etc/profile.d/graphite.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}"             >> /etc/profile.d/graphite.sh && \
  echo "export GRAPHITE_VERSION=${GRAPHITE_VERSION}" >> /etc/profile.d/graphite.sh && \
  apk update  --quiet && \
  apk upgrade --quiet && \
  apk add     --quiet --virtual .build-deps \
    build-base \
    git \
    libffi-dev \
    libressl-dev \
    py3-pip \
    python3-dev \
    tzdata && \
  apk add     --quiet \
    cairo \
    curl \
    nginx \
    python3 \
    py3-cairo \
    py3-parsing && \
  pip3 install \
    --quiet \
    --upgrade \
    pip wheel setuptools && \
  pip3 install \
    --quiet \
    supervisor==4.2.2 && \
  cp "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/timezone && \
  git clone https://github.com/graphite-project/whisper.git      /tmp/whisper      && \
  git clone https://github.com/graphite-project/carbon.git       /tmp/carbon       && \
  git clone https://github.com/graphite-project/graphite-web.git /tmp/graphite-web && \
  if [ "${BUILD_TYPE}" = "stable" ] ; then \
    for i in whisper carbon graphite-web ; do \
      echo "switch to stable Tag ${GRAPHITE_VERSION} for $i" && \
      cd /tmp/$i ; \
      git checkout "tags/${GRAPHITE_VERSION}" 2> /dev/null ; \
    done ; \
  fi && \
  # install graphite-web
  # cd /tmp/graphite-web && \
  # pip3 install --quiet --requirement requirements.txt && \
  # install whisper
  cd /tmp/whisper      && \
  pip3 install --quiet --requirement requirements.txt && \
  python3 setup.py install --quiet > /dev/null && \
  # install carbon
  cd /tmp/carbon       && \
  pip3 install --quiet --requirement requirements.txt && \
  python3 setup.py install --quiet > /dev/null && \
  # install graphite-web
  cd /tmp/graphite-web && \
  pip3 install --quiet --requirement requirements.txt && \
  python3 setup.py install --quiet > /dev/null && \
  #
  mv /opt/graphite/conf/graphite.wsgi.example /opt/graphite/webapp/graphite/graphite_wsgi.py && \
  mv /tmp/carbon/lib/carbon/tests/data/conf-directory/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf-DIST && \
  mv /tmp/carbon/lib/carbon/tests/data/conf-directory/storage-schemas.conf     /opt/graphite/conf/storage-schemas.conf-DIST && \
  apk del --quiet .build-deps && \
  rm -rf \
    /src \
    /tmp/* \
    /root/.cache \
    /var/cache/apk/* && \
  find / -type d -name __pycache__ -exec rm -rf {} \; 2> /dev/null || true

COPY rootfs/ /

WORKDIR /opt/graphite

VOLUME ["/srv", "/opt/graphite"]

CMD ["/init/run.sh"]

HEALTHCHECK \
  --interval=10s \
  --timeout=2s \
  --retries=5 \
  CMD curl --silent --fail http://localhost:8080 || exit 1

# ---------------------------------------------------------------------------------------

LABEL \
  version="${BUILD_VERSION}" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Graphite Docker Image" \
  org.label-schema.description="Inofficial Graphite Docker Image" \
  org.label-schema.url="https://graphite.readthedocs.io/en/latest/index.html" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-graphite" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${GRAPHITE_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="The Unlicense"

# ---------------------------------------------------------------------------------------
