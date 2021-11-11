FROM ruby:2.3-alpine
MAINTAINER CenturyLink Labs <clt-labs-futuretech@centurylink.com>

RUN apk --no-cache --virtual .build-deps add \
        ca-certificates \
        gcc \
        make \
        musl-dev \
        && \
    gem install --no-rdoc --no-ri docker-api json && \
    apk del .build-deps

COPY dockerfile-from-image.rb /usr/src/app/dockerfile-from-image.rb

ENTRYPOINT ["/usr/src/app/dockerfile-from-image.rb"]
CMD ["--help"]
