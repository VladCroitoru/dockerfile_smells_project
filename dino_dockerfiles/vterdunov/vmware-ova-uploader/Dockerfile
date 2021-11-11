FROM ruby:2.3-alpine

ENV BUILD_PACKAGES \
  ruby-dev \
  build-base \
  libffi-dev

ENV PACKAGES \
  libxml2-dev \
  libxslt-dev \
  curl

RUN apk add --no-cache --virtual .deps $BUILD_PACKAGES && \
    apk add --no-cache $PACKAGES && \
    gem install -N rbvmomi && \
    apk del .deps && \
    rm -rf /var/cache/apk/*

WORKDIR /usr/share/deployer

COPY cached_ovf_deploy.rb $WORKDIR
COPY deploy.sh $WORKDIR

CMD ["./deploy.sh"]
