FROM alpine:latest

MAINTAINER renoretriever <renoretriever@gmail.com>

COPY repositories /etc/apk/repositories

RUN set -x && \
    apk update && \
    apk --update add \
        build-base \
        libxml2-dev \
        libxslt-dev \
        mysql-dev \
        postgresql-dev \
        ruby \
        ruby-dev \
        ruby-rdoc \
        ruby-irb \
        nmap \
        curl && \
    gem install \
        serverspec \
        awspec \
        infrataster \
        infrataster-plugin-mysql \
        infrataster-plugin-firewall \
        infrataster-plugin-pgsql \
        infrataster-plugin-dns \
        infrataster-plugin-redis && \
    curl -fsSL https://goss.rocks/install | ash && \
    rm -rf /var/cache/apk/*

COPY json_formatter.rb /usr/lib/ruby/gems/2.4.0/gems/rspec-core-3.8.0/lib/rspec/core/formatters/json_formatter.rb
WORKDIR /root/
