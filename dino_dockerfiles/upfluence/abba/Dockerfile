FROM ruby:latest
MAINTAINER Philippe Ndiaye <phndiaye@gmail.com>

RUN apt-get update && apt-get install -y nodejs locales build-essential ruby-dev && \
  apt-get clean -y
RUN locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8
RUN mkdir -p /opt/abba
ADD . /opt/abba
ENV LC_ALL C.UTF-8

WORKDIR /opt/abba

RUN bundle install --system --without test --without development

RUN curl -sL https://github.com/upfluence/etcdenv/releases/download/v0.1.2/etcdenv-linux-amd64-0.1.2 \
  > /usr/bin/etcdenv
RUN chmod +x /usr/bin/etcdenv

RUN curl -sL https://github.com/upfluence/envtmpl/releases/download/v0.0.1/envtmpl-linux-amd64-0.0.1 \
  > /usr/bin/envtmpl
RUN chmod +x /usr/bin/envtmpl

EXPOSE 4567

ENV RACK_ENV production
ENV PORT 4567
ENV USERNAME admin
ENV PASSWORD secret

CMD ./run.sh
