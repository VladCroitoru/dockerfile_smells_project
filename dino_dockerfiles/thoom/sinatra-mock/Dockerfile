FROM ruby:alpine
MAINTAINER Z.d. Peacock <zdp@thoomtech.com>

RUN apk add --no-cache --update --virtual .build-deps build-base \
    && apk add --no-cache --update libstdc++ \
    && gem install -N \ 
           sinatra:2.0.0 \ 
           thin:1.7.1 \
    && apk del .build-deps

WORKDIR /server
COPY server .

EXPOSE 9000

CMD ["thin", "-R", "config.ru", "-p", "9000", "start"]
