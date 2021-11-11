
# Build via:
#   docker build -t my/fluentd-logzio:latest .

FROM ruby:2.2.7-alpine
RUN apk add --update \
  build-base \
  bash \
  curl \
  ca-certificates \
  libxml2 \
  libxslt \
  gcc \
  ruby \
  ruby-bundler \
  ruby-dev \
  && rm -rf /var/cache/apk/*
RUN adduser -S fluent
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.2.0/bin:$PATH
RUN gem install fluentd fluent-plugin-logzio
ADD ./fluent.conf /home/fluent/fluent.conf
ADD ./docker-entrypoint.sh /home/fluent/docker-entrypoint.sh
USER fluent
EXPOSE 24284
ENTRYPOINT ["./docker-entrypoint.sh"]
