FROM node:6

MAINTAINER Mohammad Naghavi <mohamnag@gmail.com>

RUN apt-get update && \
  apt-get install -y locales ruby && \
  gem install sass && \
  npm install -g bower@1.8.0 && \
  locale-gen en_US.UTF-8 && \
  apt-get clean && \ 
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ADD .bowerrc /.bowerrc
ADD npmrc /usr/local/etc/npmrc

CMD ["bower"]
