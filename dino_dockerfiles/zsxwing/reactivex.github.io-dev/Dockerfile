# Dev for reactivex.github.io
FROM ubuntu:14.04
MAINTAINER Shixiong Zhu <zsxwing@gmail.com>

RUN apt-get update && apt-get install -y \
  ruby \
  ruby-dev \
  nodejs \
  npm

RUN gem install jekyll uglifier rake
RUN npm install -g less
RUN ln -s /usr/bin/nodejs /usr/bin/node

ADD . /root/

EXPOSE 4000

CMD /root/start.sh
