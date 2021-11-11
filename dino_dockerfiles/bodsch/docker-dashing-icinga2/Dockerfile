
FROM bodsch/docker-dashing:2003

EXPOSE 3030

ARG BUILD_DATE
ARG BUILD_VERSION
ARG DASHBOARD
ARG ICINGA2_GEM_TYPE
ARG ICINGA2_GEM_VERSION

ENV \
  TZ='Europe/Berlin'

# ---------------------------------------------------------------------------------------

# COPY build /build

WORKDIR /opt

# hadolint ignore=SC2039,SC2045,DL3003,DL3018,DL3019
RUN \
  apk update --quiet && \
  apk add    --quiet --virtual .build-deps \
    build-base \
    git \
    ruby-dev \
    openssl-dev && \
  apk add    --quiet --no-cache \
    jq \
    tzdata \
    yajl-tools && \
  cp "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/timezone && \
  rm -rf /usr/lib/ruby/gems/current/gems/smashing/templates/project/jobs/*.rb && \
  rm -rf /usr/lib/ruby/gems/current/gems/smashing/templates/project/dashboards/*.erb && \
  smashing new "${DASHBOARD}" && \
  cd "${DASHBOARD}" && \
  echo -e "\\n \
gem 'icinga2', '~> ${ICINGA2_GEM_VERSION}'\\n" >> Gemfile && \
  mkdir -p "/opt/${DASHBOARD}/jobs" && \
  mkdir -p "/opt/${DASHBOARD}/dashboards" && \
  sed -i "/gem 'twitter'/d" Gemfile && \
  #bundle config local.icinga2 /build && \
  #if [ "${ICINGA2_GEM_TYPE}" == "local" ] ; then \
  #  for g in $(ls -1 /build/*.gem 2> /dev/null) ; do \
  #    echo "install local gem '${g}'" && \
  #    gem install --quiet --no-rdoc --no-ri "${g}" ; \
  #  done ; \
  #elif [ "${ICINGA2_GEM_TYPE}" == "stable" ] ; then \
  #  echo "gem 'icinga2', '~> ${ICINGA2_GEM_VERSION}'" >> Gemfile ; \
  #fi && \
  bundle update && \
  apk del --quiet --purge .build-deps && \
  rm -rf \
    /tmp/* \
    /build \
    /var/cache/apk/* \
    /usr/lib/ruby/gems/current/cache/* \
    /root/.gem \
    /root/.bundle

COPY rootfs/ /

WORKDIR /opt/${DASHBOARD}

CMD ["/init/run.sh"]

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD curl --silent --fail http://localhost:3030/dashing/${DASHBOARD} || exit 1

# ---------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Dashing Icinga2 Docker Image" \
  org.label-schema.description="Inofficial Dashing Icinga2 Docker Image" \
  org.label-schema.url="https://github.com/Smashing/smashing" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-dashing-icinga2" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${ICINGA_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"
