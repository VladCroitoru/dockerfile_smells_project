FROM ruby:2.7-slim
WORKDIR /app

RUN apt-get update && \
  apt-get install --no-install-recommends -y build-essential && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

ARG LITA_ENV=production
ENV LITA_ENV=$LITA_ENV
ENV PORT=80

ADD ./Gemfile /app/
ADD ./Gemfile.lock /app/

RUN if [ "$LITA_ENV" = "development" ]; then bundle install; else bundle install --without development test; fi

ADD ./ /app

EXPOSE 80

CMD ["bash", "/app/docker/start.sh"]
