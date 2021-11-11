FROM ruby:2.4-alpine
MAINTAINER WPScan Team <team@wpscan.org>

ARG BUNDLER_ARGS="--jobs=8 --without test"

COPY Gemfile Gemfile.lock /wpscan/

COPY docker /docker

RUN chmod a+x /docker/entrypoint.sh \
 && ln -sf /docker/entrypoint.sh /usr/bin/container_entrypoint \
 && adduser -h /wpscan -g WPScan -D wpscan \
 && echo "gem: --no-ri --no-rdoc" > /etc/gemrc \
 && apk upgrade --update && apk add --update --no-cache \
            # runtime dependencies
            libcurl \
            openssl-dev \
            procps \
 && apk add --no-cache --virtual build-deps \
            alpine-sdk \
            libffi-dev \
            ruby-dev \
            zlib-dev \
 && bundle install --system --gemfile=/docker/log_file_emailer/Gemfile $BUNDLER_ARGS \
 && chmod a+x /docker/log_file_emailer/log_file_emailer.rb \
 && chown -R wpscan /docker \
 && ln -sf /docker/log_file_emailer/log_file_emailer.rb /usr/bin/log_file_emailer \
 && bundle install --system --gemfile=/wpscan/Gemfile $BUNDLER_ARGS \
 && ln -sf /wpscan /usr/bin/wpscan \
 && apk del --no-cache build-deps \
 && rm -rf /var/cache/apk/* \
 && crontab -l | { cat; echo "00    00       *       *       *       wpscan /bin/sh -c \". functions.sh && run_wpscan_with_env_vars\""; } | crontab -

COPY . /wpscan

RUN chown -R wpscan:wpscan /wpscan /docker

USER wpscan

RUN /wpscan/wpscan.rb --update --verbose --no-color

WORKDIR /wpscan

ENTRYPOINT container_entrypoint

CMD ["--help"]
