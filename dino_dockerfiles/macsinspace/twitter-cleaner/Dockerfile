FROM ruby:2.4.4-alpine3.7
LABEL maintainer="Michael Usher <root@usher.is>"

RUN apk --update add --virtual build_deps ruby-dev build-base

ADD app /app
ADD scripts/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh /app/delete.rb /app/unfav.rb
RUN cd /app && bundle install --jobs=3 && apk del build_deps

ENTRYPOINT /docker-entrypoint.sh
