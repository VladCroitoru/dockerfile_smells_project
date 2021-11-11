
FROM alpine:latest

ENV \
  BUILD_DATE="2018-06-01"

EXPOSE 8080

LABEL \
  version="1802" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Markdown Service" \
  org.label-schema.description="Docker Image for an markdown Server" \
  org.label-schema.url="https://github.com/bodsch/ruby-markdown-service" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-markdown-service" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version="1.0" \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="unlicense"

# ---------------------------------------------------------------------------------------

RUN \
  apk update --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add --quiet --no-cache --virtual .build-deps \
    build-base \
    git \
    file-dev \
    ruby-dev \
    zlib-dev && \
  apk add --no-cache \
    curl \
    file \
    ruby-io-console \
    ruby-rdoc && \
  echo 'gem: --no-document' >> /etc/gemrc && \
  gem install --no-rdoc --no-ri --quiet bundle && \
  cd /srv && \
  git clone https://github.com/bodsch/ruby-markdown-service && \
  cd ruby-markdown-service && \
  bundle update --quiet && \
  apk del --quiet .build-deps && \
  rm -rf \
    /srv/ruby-markdown-service/.git \
    /tmp/* \
    /var/cache/apk/*

COPY rootfs /

WORKDIR /srv/ruby-markdown-service

VOLUME /var/www

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD curl --silent --fail http://localhost:8080/health || exit 1

ENTRYPOINT [ "/srv/ruby-markdown-service/bin/markdown.rb" ]
