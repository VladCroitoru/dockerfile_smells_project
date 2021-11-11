###
#
# A ubuntu based newrelic-twilio monitoring agent image using the latest official release when built
#
###
FROM ubuntu:14.04

WORKDIR /usr/local/newrelic_twilio_plugin-1.0.2

####
# Base stuff, software dependencies from APT
# App installation: latest version of the newrelic plugin
# cleanup after by removing dev-stuff, /tmp stuff and just leaving the app

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -qy --no-install-recommends build-essential curl ruby-dev libxml2-dev libxslt-dev ruby && \
    apt-get autoremove --purge && \
    apt-get clean && \
    gem install --no-rdoc --no-ri bundler

RUN curl -L https://github.com/newrelic-platform/newrelic_twilio_plugin/archive/1.0.2.tar.gz > latest.tar.gz && \
    tar -zxf latest.tar.gz -C /usr/local

RUN bundle install --clean --quiet --without test

RUN apt-get remove -yq --purge build-essential curl ruby-dev libxml2-dev libxslt-dev && \
    apt-get autoremove -yq --purge && \
    rm -rf latest.tar.gz /tmp/* /var/tmp/* /var/lib/apt/lists/*

COPY ./docker-entrypoint.sh /

RUN chmod 700 /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]