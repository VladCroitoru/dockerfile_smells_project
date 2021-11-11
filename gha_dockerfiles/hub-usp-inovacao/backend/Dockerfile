##########
## Base Image
##########

FROM ruby:2.7.1-alpine as base

ENV PORT=3000 \
    APP_PATH=/usr/src/app \
    HOST=0.0.0.0

WORKDIR ${APP_PATH}

RUN apk add --update \
    build-base git bash && \
    gem install rails

COPY Gemfile Gemfile.lock ./

COPY entrypoint.sh /usr/bin/

RUN chmod 755 /usr/bin/entrypoint.sh

ENTRYPOINT ["sh", "/usr/bin/entrypoint.sh"]

EXPOSE ${PORT}

CMD rails server -b ${HOST}



##########
## Development Image
##########

FROM base as development

ENV RAILS_ENV=development

RUN bundle install

COPY . ./



##########
## Production Image
##########

FROM base as production

ENV RAILS_ENV=production

RUN bundle install --without development test

COPY . ./

RUN rm -rf                                      \
    *compose.yaml Dockerfile Makefile README.md \
    scripts spec                                \
    /var/cache/apk/*
