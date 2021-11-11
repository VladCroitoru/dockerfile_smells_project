FROM ruby:2.4.1

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

ARG RAILS_ENV

WORKDIR /rails_app

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y supervisor libpq-dev python-dev && \
  apt-get clean

COPY ./Gemfile /rails_app/
COPY ./Gemfile.lock /rails_app/

RUN cd /rails_app && \
  bundle install --without test development

COPY ./ /rails_app

RUN (cd /rails_app && git log --format="%H" -n 1 > revision.txt)

COPY docker/supervisor.conf /etc/supervisor/conf.d/messenger.conf

ENV RAILS_ENV $RAILS_ENV
ENV RACK_ENV $RAILS_ENV

EXPOSE 81

ENTRYPOINT /usr/bin/supervisord
