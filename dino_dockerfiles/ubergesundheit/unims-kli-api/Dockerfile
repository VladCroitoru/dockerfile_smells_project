FROM ruby:2.5-alpine

WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/

RUN apk --no-cache add --virtual .build-deps ruby-dev build-base linux-headers \
 && bundle install --no-cache --frozen --clean \
 && rm /etc/localtime \
 && ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
 && apk del .build-deps

COPY . /usr/src/app

CMD ["unicorn", "-Ilib", "-E production"]
