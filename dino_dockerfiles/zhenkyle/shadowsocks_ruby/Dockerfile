FROM ruby:2.4
LABEL maintainer "https://github.com/zhenkyle"

EXPOSE 1080 8388

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN bundle install --without development
RUN gem build shadowsocks_ruby.gemspec
RUN gem install shadowsocks_ruby*.gem -l

CMD ["ssserver-ruby", "-h"]
