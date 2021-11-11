FROM ruby:2.3.3

LABEL maintainer="andrew@andrew-jones.com"

ENV VERSION=0.11.0

ENV RAILS_ENV=development

EXPOSE 21000

RUN mkdir /app \
    && curl -sL https://github.com/salsify/avro-schema-registry/archive/v${VERSION}.tar.gz | tar xzC /app/

WORKDIR /app/avro-schema-registry-${VERSION}
RUN bundle install

# Add our Docker specific config
# This allows you to specify the Postgres connection via the DATABASE_URL env var
COPY config/database.yml config/database.yml

CMD ["bundle", "exec", "rails", "s", "-p", "21000", "-b", "0.0.0.0"]
