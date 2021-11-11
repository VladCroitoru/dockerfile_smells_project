
FROM alpine:3.11 as stage1

ARG D3_VERSION
ARG JQ_VERSION
ARG JQUI_VERSION
ARG FONT_AWESOME
ARG SMASHING_VERSION

WORKDIR /tmp/downloads

# hadolint ignore=DL3018
RUN \
  apk update  --quiet && \
  apk add     --quiet --no-cache \
    git \
    curl

RUN \
  echo "download jquery ${JQ_VERSION}" && \
  curl \
    --silent \
    --location \
    --output /tmp/jquery.js \
    "https://code.jquery.com/jquery-${JQ_VERSION}.min.js"

RUN \
  echo "download jquery-ui ${JQUI_VERSION}" && \
  curl \
    --silent \
    --location \
    --output "jquery-ui-${JQUI_VERSION}.zip" \
     "https://jqueryui.com/resources/download/jquery-ui-${JQUI_VERSION}.zip"

RUN \
  echo "download fontawesome ${FONT_AWESOME}" && \
  curl \
    --silent \
    --location \
    --output "font-awesome-${FONT_AWESOME}.zip" \
    "https://fontawesome.com/v${FONT_AWESOME}/assets/font-awesome-${FONT_AWESOME}.zip"

RUN \
  echo "download jQuery-Knob" && \
  git clone https://github.com/aterrien/jQuery-Knob.git 2> /dev/null && \
  mv jQuery-Knob/js/jquery.knob.js /tmp/jquery.knob.js

RUN \
  echo "download rickshaw" && \
  git clone https://github.com/shutterstock/rickshaw.git 2> /dev/null && \
  mv rickshaw/rickshaw.min.js /tmp/rickshaw.min.js


RUN \
  echo "download d3 ${D3_VERSION}" && \
  curl \
    --silent \
    --location \
    --output d3.zip \
    "https://github.com/d3/d3/releases/download/v${D3_VERSION}/d3.zip" && \
  unzip d3.zip > /dev/null && \
  mv d3.*js /tmp/

RUN \
  unzip "jquery-ui-${JQUI_VERSION}.zip" -d /tmp/ > /dev/null && \
  mv "/tmp/jquery-ui-${JQUI_VERSION}" /tmp/jquery-ui

RUN \
  unzip "font-awesome-${FONT_AWESOME}.zip" -d /tmp/ > /dev/null && \
  mv "/tmp/font-awesome-${FONT_AWESOME}" /tmp/font-awesome

# ---------------------------------------------------------------------------------------

FROM alpine:3.11

EXPOSE 3030

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION

ENV \
  TERM=xterm \
  TZ='Europe/Berlin'

# ---------------------------------------------------------------------------------------

WORKDIR /opt

# hadolint ignore=SC2039,SC2046,DL3017,DL3018,DL3028
RUN \
  apk update  --quiet && \
  apk upgrade --quiet && \
  apk add     --quiet --no-cache --virtual .build-deps \
    build-base \
    ruby-dev \
    libffi-dev && \
  apk add     --quiet --no-cache  \
    curl \
    nodejs \
    ruby \
    ruby-io-console \
    tzdata && \
  echo 'gem: --no-document' >> /etc/gemrc && \
  echo -e "source 'https://rubygems.org'\\n \
gem 'smashing', '~> 1.1'\\n\
gem 'puma', '~> 3.12'\\n\
gem 'json', '~> 2.1'\\n\
gem 'etc', '~> 1.0'\\n" > /opt/Gemfile && \
  gem install bundle && \
  bundle update --quiet && \
  ln -s $(ls -1 /usr/lib/ruby/gems)                          /usr/lib/ruby/gems/current && \
  ln -s $(ls -d1 /usr/lib/ruby/gems/current/gems/smashing-*) /usr/lib/ruby/gems/current/gems/smashing && \
  apk del --quiet --purge .build-deps && \
  rm -rf \
    /tmp/* \
    /build \
    /var/cache/apk/* \
    /usr/lib/ruby/gems/current/cache/* \
    /root/.gem \
    /root/.bundle

COPY --from=stage1 /tmp/jquery.js               /usr/lib/ruby/gems/current/gems/smashing/javascripts/
COPY --from=stage1 /tmp/d3.*.js                 /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/javascripts/
COPY --from=stage1 /tmp/jquery.knob.js          /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/javascripts/
COPY --from=stage1 /tmp/rickshaw.min.js         /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/javascripts/
COPY --from=stage1 /tmp/jquery-ui/*.min.js      /usr/lib/ruby/gems/current/gems/smashing/javascripts/
COPY --from=stage1 /tmp/jquery-ui/*.min.css     /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/stylesheets/
COPY --from=stage1 /tmp/jquery-ui/images/*      /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/images/
COPY --from=stage1 /tmp/font-awesome/fonts/*    /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/fonts/
COPY --from=stage1 /tmp/font-awesome/css/*.css  /usr/lib/ruby/gems/current/gems/smashing/templates/project/assets/stylesheets/

# ---------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Smashing Docker Image" \
  org.label-schema.description="Inofficial Smashing Docker Image" \
  org.label-schema.url="https://github.com/Smashing/smashing" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-dashing" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${SMASHING_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"

# ---------------------------------------------------------------------------------------
