FROM centurylink/ruby-base:2.2

MAINTAINER CenturyLink Labs <innovationlabs@ctl.io>

ENV RAILS_VERSION 4.2.3

RUN \
  apt-get update && \
  curl --silent --location https://deb.nodesource.com/setup_0.12 | bash - && \
  # install database dependencies
  apt-get install -y nodejs --no-install-recommends && \

  # rails
  gem install rails --version "$RAILS_VERSION" && \

  # cleanup
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
  rm -rf ~/.gem

EXPOSE 3000
