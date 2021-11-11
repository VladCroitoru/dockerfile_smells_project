FROM ruby:2.5-alpine

RUN apk --no-cache add make gcc libc-dev

VOLUME /apinfo
ADD . /apinfo
RUN cd /apinfo && bundle install

WORKDIR /apinfo
CMD ["puma", "-C", "config/puma.rb"]
