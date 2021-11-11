FROM ruby:latest
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN groupadd -r runner -g 433 \
    && useradd -u 431 -r -g runner -m -s /sbin/nologin -c "Docker runner user" runner

USER runner

WORKDIR /home/runner

RUN git clone https://github.com/oVirt/ovirt-site \
    && cd ovirt-site \
    && git submodule init && git submodule update \
    && bundle install --path ~/.gem

EXPOSE 4567

CMD cd ovirt-site && bundle exec middleman
