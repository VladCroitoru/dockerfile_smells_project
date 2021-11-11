FROM ruby:3.0.2-alpine

LABEL org.opencontainers.image.authors="daz.oakley@gmail.com"

RUN apk update && \
  apk upgrade && \
  apk add build-base ruby-dev libxml2-dev libxslt-dev postgresql-dev mysql-dev openssl ca-certificates wget && \
  update-ca-certificates && \
  rm -rf /var/cache/apk/*

RUN addgroup bandiera && \
  adduser -D -G bandiera -h /home/bandiera bandiera

WORKDIR /home/bandiera

RUN gem install bundler

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN bundle config set --local without 'test' && \
  bundle config set --local deployment 'true' && \
  bundle config set --local frozen 'true' && \
  bundle install --jobs 4

COPY . .

USER bandiera

ENV RACK_ENV=production

EXPOSE 5000

CMD ["./entrypoint.sh"]
