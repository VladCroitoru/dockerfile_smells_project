FROM ruby:2.3.5-slim

RUN ["/bin/bash", "-c", "set -o pipefail \
  && apt-get update \
  && apt-get -y install apt-transport-https curl \
  && echo \"deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main\" > /etc/apt/sources.list.d/pgdg.list \
  && curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt-get update \
  && apt-get -y install \
      git \
      libpq-dev \
      libreadline-dev\
      nodejs \
      postgresql-client-9.4 \
      imagemagick \
      build-essential \ 
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && gem install bundler \
  && curl -o- -L https://yarnpkg.com/install.sh | bash"]
