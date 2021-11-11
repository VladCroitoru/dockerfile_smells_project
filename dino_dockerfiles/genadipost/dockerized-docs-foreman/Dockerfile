FROM ruby:latest
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN groupadd -r runner -g 433 \
    && useradd -u 431 -r -g runner -m -s /sbin/nologin -c "Docker runner user" runner

USER runner

WORKDIR /home/runner

RUN git clone https://github.com/theforeman/theforeman.org \
    && cd theforeman.org \
    && bundle install --path ~/.gem

EXPOSE 8080

CMD cd theforeman.org && bundle exec jekyll serve -H 0.0.0.0 -P 8080
