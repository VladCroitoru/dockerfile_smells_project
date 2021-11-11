FROM ruby:1.9.3
MAINTAINER lukewpatterson

RUN gem install github-pages
# https://github.com/sstephenson/execjs#execjs
RUN gem install therubyracer

EXPOSE 4000
VOLUME /gh-pages

WORKDIR /gh-pages
CMD ["jekyll", "serve", "--force_polling"]
