FROM ruby:3.0.2

RUN mkdir /data
WORKDIR /data

COPY ./sources.list /etc/apt/sources.list

RUN apt-get update && apt-get -y install nodejs

COPY . /data/

RUN gem sources --add https://mirrors.tuna.tsinghua.edu.cn/rubygems/ --remove https://rubygems.org/

RUN gem install bundler

RUN bundle config mirror.https://rubygems.org https://mirrors.tuna.tsinghua.edu.cn/rubygems

RUN bundle install

ENV LANG en_US.UTF-8

VOLUME /data

EXPOSE 80

CMD bundle exec jekyll build && bundle exec jekyll serve --host 0.0.0.0 --port 80
