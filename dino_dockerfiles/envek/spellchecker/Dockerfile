FROM jruby:9-alpine
LABEL maintainer="Andrey Novikov <envek@evilmartians.com>"

ENV RACK_ENV=production PORT=5000

WORKDIR /app

COPY Gemfile /app/
COPY Gemfile.lock /app/

RUN  apk --no-cache update && \
     apk --no-cache upgrade && \
     apk add hunspell curl git && \
     gem install bundler && \
     bundle install && \
     apk del git

RUN mkdir -p /usr/share/hunspell/ && \
   curl 'https://cgit.freedesktop.org/libreoffice/dictionaries/plain/ru_RU/ru_RU.{dic,aff}' -o '/usr/share/hunspell/ru_RU.#1'


ADD . /app
WORKDIR /app

EXPOSE $PORT

HEALTHCHECK CMD curl -f -X POST -d '{"query": "Плптье женское"}' http://localhost:$PORT/ || exit 1

CMD bundle exec rackup -s puma -p $PORT -o 0.0.0.0 -O "Threads=0:${MAX_THREADS:-16}"
