FROM ruby:2.4.1-alpine

LABEL maintainer "kyontan <kyontan@monora.me>"

WORKDIR /usr/src/app

ADD Gemfile Gemfile.lock /usr/src/app/

# RUN apt-get update && apt-get install -y libqt4-dev libqtwebkit-dev xvfb fonts-ipafont fonts-ipafont-gothic fonts-ipafont-mincho
RUN apk update \
 && apk add --virtual .build-dep \
        build-base \
 && bundle install \
 && apk del .build-dep \
 && rm -rf /var/cache/apk/*

ADD crawl.rb /usr/src/app/crawl.rb

CMD ["bundle", "exec", "ruby", "crawl.rb"]
