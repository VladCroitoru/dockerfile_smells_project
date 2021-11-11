FROM ruby:2.3-alpine
MAINTAINER Ross Fairbanks "ross@microscaling.com"

# Cache installing gems
WORKDIR /tmp
COPY Gemfile* /tmp/

# Update and install all of the required packages.
# At the end, remove the apk cache
RUN apk update && \
    apk upgrade && \
    bundle install && \
    rm -rf /var/cache/apk/*

# Create working directory.
WORKDIR /app

COPY . ./
COPY marathon_apps/ /apps/marathon/

LABEL com.microscaling.is-scalable="True" \
  com.microscaling.priority="1" \
  com.microscaling.max-delta="2" \
  com.microscaling.min-containers="1" \
  com.microscaling.max-containers="10"

ENTRYPOINT ["bundle", "exec", "rake"]

# By default start the consumer to read messages from the queue.
CMD ["consumer"]
