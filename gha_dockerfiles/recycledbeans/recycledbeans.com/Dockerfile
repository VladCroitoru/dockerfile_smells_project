FROM node:14-buster

RUN mkdir /var/jekyll
WORKDIR /var/jekyll

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y ruby ruby-dev

RUN cd /var/jekyll

COPY Gemfile ./
COPY Gemfile.lock ./

RUN echo '#!/bin/bash' > /root/script.sh
RUN echo "yarn install && yarn run prod" >> /root/script.sh
RUN echo "yarn run version" >> /root/script.sh
#RUN echo "rm Gemfile.lock" >> /root/script.sh
# RUN echo "bundle install" >> /root/script.sh
RUN echo "bundle exec jekyll build" >> /root/script.sh

RUN gem install bundler
RUN bundle install

RUN echo "$PWD"

CMD ["bash", "/root/script.sh"]
