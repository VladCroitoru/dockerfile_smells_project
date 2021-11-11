FROM ruby:2.6-slim-stretch

WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ARG REVISION=''
ENV REVISION=$REVISION
ARG RAILS_ENV=production
ENV RAILS_ENV=$RAILS_ENV

ADD ./Gemfile /app/
ADD ./Gemfile.lock /app/

RUN bundle config --global jobs `cat /proc/cpuinfo | grep processor | wc -l | xargs -I % expr % - 1` && \
  if echo "development test" | grep -w "$RAILS_ENV"; then \
  bundle install; \
  else bundle install --without development test; fi

ADD ./ /app

EXPOSE 80

CMD ["/app/scripts/docker/start.sh"]
