# wow Docker files

FROM ruby:2.3.1-alpine
MAINTAINER <ak.hisashi@gmail.com>

RUN apk --update --upgrade add git && \
  rm /var/cache/apk/*

# git clone
RUN git clone https://github.com/kazuhisa/wow.git

# bundle install
RUN cd /wow && bundle install

CMD cd /wow && bundle exec ruby wow.rb
